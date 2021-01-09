import sys
from clint.textui import colored
from lexer import Lexer

def get_input():
	data = str(input(">>>"))
	return data

# all the arguments
ARGUMENTS = sys.argv
ARGUMENTS = ARGUMENTS[1:len(ARGUMENTS)]


condition = True
while condition:
	data = get_input()

	if data == "stop":
		condition = False
	else:
		l = Lexer(data)
		l.start_evaluation()