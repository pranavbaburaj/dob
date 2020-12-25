import sys
from src.arguments import ArgumentParser
from src.parser.variables.declarations import *


ARGUMENTS = sys.argv
ARGUMENTS = ARGUMENTS[1:len(ARGUMENTS)]

argument_parser = ArgumentParser(ARGUMENTS)





