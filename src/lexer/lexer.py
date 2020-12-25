import sys
from .token.tokens import *
from .token.generate import TokenGenerator as Tokens
from .types.make_numbers import *
from .types.strings import *
from clint.textui import colored



class KeyWordSearch():
    def __init__(self, pos, data):
        self.data = data
        self.pos = pos
        self.success = True
        self.n = ""

    def curr_(self):
        if self.pos == len(self.data):
            return None
        else:
            return self.data[self.pos]

    def start(self):
        curr = self.curr_()
        while curr is not None and curr is not " ":
            self.n += str(curr)

            self.pos += 1
            curr = self.curr_()

        return self.n, self.pos, self.success
            



class Lexer():
    def __init__(self, data, x):
        self.data = data
        self.tokens = []
        self.line = x + 1
        self.pos = 0
        self.start_evaluation()

    def set_current_character(self):

        if self.pos == len(self.data):
            return None
        else:
            return self.data[self.pos]

    

    def start_evaluation(self):
        self.curr = self.set_current_character()


        while self.curr is not None:
            # characters = self.check_for_tokens(self.curr)
            if str(self.curr) == "+":
                self.tokens.append(Tokens("+", ADD))
            elif str(self.curr) == " ":
                pass
            elif str(self.curr) == "-":
                self.tokens.append(Tokens("-", SUB))
            # elif str(self.curr) == "(":
            #     self.tokens.append(Tokens("(", LPAREN))
            # elif str(self.curr) == ")":
            #     self.tokens.append(Tokens(")", RPAREN))
            elif str(self.curr) == "*":
                self.tokens.append(Tokens("*", MUL))
            elif str(self.curr) == "/":
                self.tokens.append(Tokens("/", DIV))
            elif str(self.curr) in NUMS:
                data = Numbers(self.pos, self.data).make_num()
                self.pos = data[0] - 1
                self.tokens.append(Tokens(data[1], data[2]))
            elif str(self.curr) in CHARS:
                str_ = Strings(self.pos, self.data).startEval()
                self.pos = str_["pos"]
                self.tokens.append(Tokens(str_["data"], str_["type"]))
            elif str(self.curr) == "\n":
                self.line += 1
            elif str(self.curr) == "(":
                pass
            elif str(self.curr) == ")":
                pass
            elif str(self.curr) == ",":
                pass
            elif str(self.curr) == "=":
                self.tokens.append(Tokens("=", "VAR"))
            else:
                key_ = KeyWordSearch(self.pos, self.data)
                data = key_.start()
                self.pos = data[1] - 1
                if not data[2]:
                    print(colored.red(
                        f"Invalid character {self.curr} at line {self.line}"
                    ))
                    break
                else:
                    self.tokens.append(Tokens(data[0], "NAME"))


            self.pos += 1
            self.curr = self.set_current_character()
        return self.tokens

