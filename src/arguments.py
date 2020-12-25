from clint.textui import colored
from .reader.file_reader import FileReader
from .lexer.lexer import Lexer
from .parser.parser import Parser
from .application.app_info import APPLICATION_VERSION

ARGUMENT_KEYWORDS = [
    "-v", "-h", "shell"
]



class ArgumentError():
    def __init__(self, error):
        self.error = error

    def __repr__(self):
        return self.error

class ArgumentParser():
    def __init__(self, arguments):
        self.args = arguments
        self.argument_exists()

    def argument_exists(self):
        for index, element in enumerate(self.args):
            if element in ARGUMENT_KEYWORDS:
                if element == "shell":
                    condition = True
                    line_ = 1
                    while condition:
                        command = str(input("dob>>>"))

                        if command == ".exit":
                            condition = False
                        else:
                            l = Lexer(command, line_)
                            lex = l.start_evaluation()
                            parse = Parser(lex)
                        line_ += 1
                elif element == "-v":
                    print(
                        colored.blue(APPLICATION_VERSION)
                    )
            else:
                if element.endswith(".dob"):
                    file_read = FileReader(element)
                    lines = file_read.read()
                    token_array = []
                    for x in range(len(lines)):
                        lexer = Lexer(lines[x], x)
                        token_array.append(lexer.start_evaluation())
                    for i in range(len(token_array)):
                        parser = Parser(token_array[i])
                else:
                    error = ArgumentError(f"Unexpected argument {element}")
                    print(colored.red(error))


    def __repr__(self):
        return str(self.args[0])