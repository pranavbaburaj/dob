from clint.textui import colored

class DefinitionError():
    def __init__(self, undeclared_variable):
        self.var = undeclared_variable
        self.evoke()

    def evoke(self):
        print(colored.red(
            f"Definition Error"
        ))
        print(colored.red(
            f"=================="
        ))
        print(colored.red(
            f"{self.var} is not defined"
        ))

