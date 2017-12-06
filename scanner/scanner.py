"""
Contains scanner, which divides source text onto different parts.
"""

import collections
import itertools as _itertools
import re
import sys
from tokenlist import Token, TOKEN_DICT


cookie_re = re.compile(r'^[ \t\f]*#.*?coding[:=][ \t]*([-\w.]+)', re.ASCII)
blank_re = re.compile(br'^[ \t\f]*(?:[#\r\n]|$)', re.ASCII)


def group(*choices): return '(' + '|'.join(choices) + ')'
def any(*choices): return group(*choices) + '*'
def maybe(*choices): return group(*choices) + '?'

# Note: we use unicode matching for names ("\w") but ascii matching for
# number literals.
Whitespace = r'[ \f\t]*'
Comment = r'#[^\r\n]*'
Ignore = Whitespace + any(r'\\\r?\n' + Whitespace) + maybe(Comment)
Name = r'\w+'

Hexnumber = r'0[xX](?:_?[0-9a-fA-F])+'
Binnumber = r'0[bB](?:_?[01])+'
Octnumber = r'0[oO](?:_?[0-7])+'
Decnumber = r'(?:0(?:_?0)*|[1-9](?:_?[0-9])*)'
Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
Exponent = r'[eE][-+]?[0-9](?:_?[0-9])*'
Pointfloat = group(r'[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?',
                   r'\.[0-9](?:_?[0-9])*') + maybe(Exponent)
Expfloat = r'[0-9](?:_?[0-9])*' + Exponent
Floatnumber = group(Pointfloat, Expfloat)
Imagnumber = group(r'[0-9](?:_?[0-9])*[jJ]', Floatnumber + r'[jJ]')
Number = group(Imagnumber, Floatnumber, Intnumber)

# Return the empty string, plus all of the valid string prefixes.
def _all_string_prefixes():
    # The valid string prefixes. Only contain the lower case versions,
    #  and don't contain any permuations (include 'fr', but not
    #  'rf'). The various permutations will be generated.
    _valid_string_prefixes = ['b', 'r', 'u', 'f', 'br', 'fr']
    # if we add binary f-strings, add: ['fb', 'fbr']
    result = {''}
    for prefix in _valid_string_prefixes:
        for t in _itertools.permutations(prefix):
            # create a list with upper and lower versions of each
            #  character
            for u in _itertools.product(*[(c, c.upper()) for c in t]):
                result.add(''.join(u))
    return result

def _compile(expr):
    return re.compile(expr, re.UNICODE)

# Note that since _all_string_prefixes includes the empty string,
#  StringPrefix can be the empty string (making it optional).
StringPrefix = group(*_all_string_prefixes())

# Tail end of ' string.
Single = r"[^'\\]*(?:\\.[^'\\]*)*'"
# Tail end of " string.
Double = r'[^"\\]*(?:\\.[^"\\]*)*"'
# Tail end of ''' string.
Single3 = r"[^'\\]*(?:(?:\\.|'(?!''))[^'\\]*)*'''"
# Tail end of """ string.
Double3 = r'[^"\\]*(?:(?:\\.|"(?!""))[^"\\]*)*"""'
Triple = group(StringPrefix + "'''", StringPrefix + '"""')
# Single-line ' or " string.
String = group(StringPrefix + r"'[^\n'\\]*(?:\\.[^\n'\\]*)*'",
               StringPrefix + r'"[^\n"\\]*(?:\\.[^\n"\\]*)*"')

# Because of leftmost-then-longest match semantics, be sure to put the
# longest operators first (e.g., if = came before ==, == would get
# recognized as two instances of =).
Operator = group(r"\*\*=?", r">>=?", r"<<=?", r"!=",
                 r"//=?", r"->",
                 r"[+\-*/%&@|^=<>]=?",
                 r"~")

Bracket = '[][(){}]'
Special = group(r'\r?\n', r'\.\.\.', r'[:;.,@]')
Funny = group(Operator, Bracket, Special)

PlainToken = group(Number, Funny, String, Name)
#Token = Ignore + PlainToken  # overwrites imported Token from tokenlist

# First (or only) line of ' or " string.
ContStr = group(StringPrefix + r"'[^\n'\\]*(?:\\.[^\n'\\]*)*" +
                group("'", r'\\\r?\n'),
                StringPrefix + r'"[^\n"\\]*(?:\\.[^\n"\\]*)*' +
                group('"', r'\\\r?\n'))
PseudoExtras = group(r'\\\r?\n|\Z', Comment, Triple)
PseudoToken = Whitespace + group(PseudoExtras, Number, Funny, ContStr, Name)

# For a given string prefix plus quotes, endpats maps it to a regex
#  to match the remainder of that string. _prefix can be empty, for
#  a normal single or triple quoted string (with no prefix).
endpats = {}
for _prefix in _all_string_prefixes():
    endpats[_prefix + "'"] = Single
    endpats[_prefix + '"'] = Double
    endpats[_prefix + "'''"] = Single3
    endpats[_prefix + '"""'] = Double3

# A set of all of the single and triple quoted string prefixes,
#  including the opening quotes.
single_quoted = set()
triple_quoted = set()
for t in _all_string_prefixes():
    for u in (t + '"', t + "'"):
        single_quoted.add(u)
    for u in (t + '"""', t + "'''"):
        triple_quoted.add(u)

tabsize = 8

class TokenError(Exception): pass


def tokenize(source_code):
    """ Simply creates tokens from source code in string.
    """
    tokens = []
    line_number = parenlev = continued = 0
    numchars = '0123456789'
    contstr, needcont = '', 0
    contline = None
    indents = [0]

    print(f'source code inside = {source_code}')
    amount_of_lines = len(source_code.split("\n"))
    print(f'lines amount: {amount_of_lines}')

    for line in source_code.split('\n'):

        print(f'current_line: {line}')
        line_number += 1
        chars_in_line = len(line)
        char_number = 0

        if contstr:                            # continued string
            if not line:
                raise TokenError("EOF in multi-line string", token_starts)
            endmatch = endprog.match(line)
            if endmatch:
                char_number = end = endmatch.end(0)
                tokens.append(Token(name='STRING', text=contstr + line[:end],
                       starts=token_starts, ends=(line_number, end), context=contline + line))
                contstr, needcont = '', 0
                contline = None
            elif needcont and line[-2:] != '\\\n' and line[-3:] != '\\\r\n':
                tokens.append(Token(name='ERRORTOKEN', text=contstr + line,
                           starts=token_starts, ends=(line_number, len(line)), context=contline))
                contstr = ''
                contline = None
                continue
            else:
                contstr = contstr + line
                contline = contline + line
                continue

        elif parenlev == 0 and not continued:  # new statement
            if not line:
                continue
            column = 0
            while char_number < chars_in_line:                   # measure leading whitespace
                if line[char_number] == ' ':
                    column += 1
                elif line[char_number] == '\t':
                    column = (column//tabsize + 1)*tabsize
                elif line[char_number] == '\f':
                    column = 0
                else:
                    break
                char_number += 1
            if char_number == chars_in_line:
                break

            if line[char_number] in '#\r\n':           # skip comments or blank lines
                if line[char_number] == '#':
                    comment_token = line[char_number:].rstrip('\r\n')
                    tokens.append(Token(name='COMMENT', text=comment_token, starts=(line_number, char_number),
                                        ends=(line_number, char_number + len(comment_token)), context=line))
                    char_number += len(comment_token)

                tokens.append(Token(name='NL', text=line[char_number:],
                           starts=(line_number, char_number), ends=(line_number, len(line)),
                           context=line))
                continue

            if column > indents[-1]:           # count indents or dedents
                indents.append(column)
                tokens.append(Token(name='INDENT', text=line[:char_number], starts=(line_number, 0),
                                    ends=(line_number, char_number), context=line))
            while column < indents[-1]:
                if column not in indents:
                    raise IndentationError(
                        "unindent does not match any outer indentation level",
                        ("<tokenize>", line_number, char_number, line))
                indents = indents[:-1]

                tokens.append(Token(name='DEDENT', starts=(line_number, char_number),
                                    ends=(line_number, char_number), context=line))

        else:                                  # continued statement
            if not line:
                raise TokenError("EOF in multi-line statement", (line_number, 0))
            continued = 0


        while char_number < chars_in_line:
            pseudomatch = _compile(PseudoToken).match(line, char_number)
            if pseudomatch:                                # scan for tokens
                start, end = pseudomatch.span(1)
                spos, epos, char_number = (line_number, start), (line_number, end), end
                if start == end:
                    continue
                token, initial = line[start:end], line[start]

                if (initial in numchars or                  # ordinary number
                    (initial == '.' and token != '.' and token != '...')):
                    tokens.append(Token(name='NUMBER', text=token, starts=spos, ends=epos, context=line))
                elif initial in '\r\n':
                    if parenlev > 0:
                        tokens.append(Token(name='NL', text=token, starts=spos, ends=epos, context=line))
                    else:
                        tokens.append(Token(name='NEWLINE', text=token, starts=spos, ends=epos, context=line))

                elif initial == '#':
                    assert not token.endswith("\n")
                    tokens.append(Token(name='COMMENT', text=token, starts=spos, ends=epos, context=line))

                elif token in triple_quoted:
                    endprog = _compile(endpats[token])
                    endmatch = endprog.match(line, char_number)
                    if endmatch:                           # all on one line
                        char_number = endmatch.end(0)
                        token = line[start:char_number]
                        tokens.append(Token(name='STRING', text=token, starts=spos,
                                            ends=(line_number, char_number), context=line))
                    else:
                        token_starts = (line_number, start)           # multiple lines
                        contstr = line[start:]
                        contline = line
                        break

                # Check up to the first 3 chars of the token to see if
                #  they're in the single_quoted set. If so, they start
                #  a string.
                # We're using the first 3, because we're looking for
                #  "rb'" (for example) at the start of the token. If
                #  we switch to longer prefixes, this needs to be
                #  adjusted.
                # Note that initial == token[:1].
                # Also note that single quote checking must come after
                #  triple quote checking (above).
                elif (initial in single_quoted or
                      token[:2] in single_quoted or
                      token[:3] in single_quoted):
                    if token[-1] == '\n':                  # continued string
                        token_starts = (line_number, start)
                        # Again, using the first 3 chars of the
                        #  token. This is looking for the matching end
                        #  regex for the correct type of quote
                        #  character. So it's really looking for
                        #  endpats["'"] or endpats['"'], by trying to
                        #  skip string prefix characters, if any.
                        endprog = _compile(endpats.get(initial) or
                                           endpats.get(token[1]) or
                                           endpats.get(token[2]))
                        contstr, needcont = line[start:], 1
                        contline = line
                        break
                    else:                                  # ordinary string
                        tokens.append(Token(name='STRING', text=token, starts=spos, ends=epos, context=line))

                elif initial.isidentifier():               # ordinary name
                    tokens.append(Token(name='NAME', text=token, starts=spos, ends=epos, context=line))
                elif initial == '\\':                      # continued stmt
                    continued = 1
                else:
                    if initial in '([{':
                        parenlev += 1
                    elif initial in ')]}':
                        parenlev -= 1
                    tokens.append(Token(name='OP', text=token, starts=spos, ends=epos, context=line))
            else:
                tokens.append(Token(name='ERRORTOKEN', text=line[char_number], starts=(line_number, char_number),
                                    ends=(line_number, char_number+1), context=line))
                char_number += 1


    tokens.append(Token(name='ENDMARKER', starts=(line_number, 0), ends=(line_number, 0)))
    return tokens
