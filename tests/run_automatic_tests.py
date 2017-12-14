import os, os.path
import pytest


files_dir = os.path.dirname(__file__)
os.chdir()

pytest.main(['test_import.py'])
