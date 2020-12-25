from clint.textui import colored

class Syntax_Error():
    def __init__(self):
        self.evoke()

    def evoke(self):
        print(colored.red(
            f"Syntax Error"
        ))
        print(colored.red(
            f"=================="
        ))
        print(colored.red(
            f"Invalid syntax"
        ))

