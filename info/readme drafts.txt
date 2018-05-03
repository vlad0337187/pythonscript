#####
#####
Indents in definitions


'->' and '<-' are the same as 'indent' and 'dedent'
Not more, not less. For example, if we'll place '->' after list token, than parser will wait until nearest dedent or '<-'.


# wrong:
list -> 1, 2, 3, 4
	5, 6    # indent 2

Here indent 2 will cause error, because indent for block list definition was made with arrow token '->'.
And indent 2 is treated as indent, where methods on this list can be called.


If you want to make list definition inline using arrow indents, than you must place arrow dedent too.
For example, this could be used in list definition inside of other list:


list
	1, 3, '45', list -> 1, 2, 3 <-, 18, 21

or so:

list
	1 3 '45'
	list -> 1 2 3
	<-
	18 21

(commas are optional)


But it seems to be excessive. It will allow you to do such things, like continuing definition on new line:


list
	1 3 '45' list -> 1 2
	3 4 <-
	18 21


(here we continued to define nested list on the next line)


But if all list will only be on one line, you could just specify list elements after 'list' keyword,
that definition will be on the same line, and to the end of line (or to ';', which is the same)


list 1 2 'df' 3 8


Also it's possible to nest such definitions one into other:


list 1 2 'df' list 1 2; 3 8


It's equivalent to Python's [1, 2, 'df', [1, 2], 3, 8]


Methods could be called just after indent after definition:


list 1 2 3
	.reverse()
	.sort()

list
	1 2 3
	4 5 6
	7 8 9
		.reverse()

list 1 2 3 -> .reverse() <-


Points before method are optional, also newlines before next method are optional,
also 'do' operator could be used to call method instead of parenthesises:


list 1 2 3
	reverse() sort()

list
	1 2 3
	4 5 6
		do reverse
		do sort

list 1 2 3
	do reverse; do sort


(because after do and function name parser expects or passed to method arguments,
or indent (to start block, in which arguments will be passed to method),
than to show that no arguments are passed you could use new line, or ';')





#####
#####
Calling functions.

Indents in calling functions are the same.


Calling functions with passing arguments using block indent:


function_1
	argument_1   argument_2  argument_3
	function_2() argument_5  argument_6


Of course, you can use arrow indents here:


function_1 -> argument_1   argument_2  argument_3
function_2() argument_5  argument_6
<-


But probably sometimes is better to just pass arguments by writting them just
after fucntion name:


function_1  argument_1  argument_2  argument_3


Calling methods on returned by functions values
