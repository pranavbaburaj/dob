from .operations.operations import Operators as op
from clint.textui import colored
from .variables.declarations import *
from .variables.variables import Variables
from .errors.definition import DefinitionError as DefErr
from .errors.syntax import Syntax_Error
from .modules.os import OperatingSystemFunctions as Os
from .modules.file import File as FileManager
from src.database.db import Database
from .admin.admin import *

NUMS = [
    "INT", "FLOAT"
]

OS_FUNCTIONS = [
    "os", "node", "processor",
    "location"
]

ALL_DATABASES = []

class Parser():
    def __init__(self, line_to_parser):
        self.data = line_to_parser
        self.eval_()

    def eval_(self):
        for index, element in enumerate(self.data):
            SPLITTED_TOKEN = str(element).split(":")
            if SPLITTED_TOKEN[-1] == "ADD":
                ADDENDS = [
                    str(self.data[index - 1]).split(":"),
                    str(self.data[index + 1]).split(":")
                ]
                if ADDENDS[0][-1] in NUMS and ADDENDS[1][-1] in NUMS:
                    return_value = op.add(ADDENDS[0][0], ADDENDS[1][0])
                    self.data[index] = return_value
                    self.data.pop(index - 1)
                    self.data.pop(index)
            elif SPLITTED_TOKEN[-1] == "MUL":
                ADDENDS = [
                    str(self.data[index - 1]).split(":"),
                    str(self.data[index + 1]).split(":")
                ]
                if ADDENDS[0][-1] in NUMS and ADDENDS[1][-1] in NUMS:
                    return_value = op.mul(ADDENDS[0][0], ADDENDS[1][0])
                    self.data[index] = return_value
                    self.data.pop(index - 1)
                    self.data.pop(index)
            elif SPLITTED_TOKEN[-1] == "DIV":
                ADDENDS = [
                    str(self.data[index - 1]).split(":"),
                    str(self.data[index + 1]).split(":")
                ]
                if ADDENDS[0][-1] in NUMS and ADDENDS[1][-1] in NUMS:
                    return_value = op.div(ADDENDS[0][0], ADDENDS[1][0])
                    self.data[index] = return_value
                    self.data.pop(index - 1)
                    self.data.pop(index)
            elif SPLITTED_TOKEN[-1] == "SUB":
                ADDENDS = [
                    str(self.data[index - 1]).split(":"),
                    str(self.data[index + 1]).split(":")
                ]
                if ADDENDS[0][-1] in NUMS and ADDENDS[1][-1] in NUMS:
                    return_value = op.sub(ADDENDS[0][0], ADDENDS[1][0])
                    self.data[index] = return_value
                    self.data.pop(index - 1)
                    self.data.pop(index)
            elif SPLITTED_TOKEN[-1] == "NAME":
                e = str(element).split(":")
                parsed_var = e[0].split("~")
                if parsed_var[0] == "var":
                    var_ = str(parsed_var[-1]).split("=")
                    new_var = Variables(var_[-1])
                    VARIABLES[str(var_[0])] = new_var.get_formatted()
                elif parsed_var[0] == "file":
                    FileManager.create(str(parsed_var[1]))
                elif parsed_var[0] == "print_var":
                    if parsed_var[-1] in VARIABLES:
                        var_out = VARIABLES[str(parsed_var[-1])]['value']
                        print(str(var_out).replace('"', ''))
                    else:
                        del_error = DefErr(str(parsed_var[-1]))
                elif parsed_var[0] in OS_FUNCTIONS:
                    tok = parsed_var[0]
                    if tok == "os":
                        print(Os.os_name())
                    elif tok == "node":
                        print(Os.node())
                    elif tok == "processor":
                        print(Os.processor())
                    elif tok == "location":
                        print(Os.location())
                elif parsed_var[0] == "create":
                    db = Database()
                    ALL_DATABASES.append(db)
                    DATABASES.append(db)
                    db.commit()
                elif parsed_var[0] == "admin":
                    run()
                elif parsed_var[0] == "add":
                    data = parsed_var[1]
                    if data.endswith(")") and data.startswith("("):
                        data = data[:len(data) - 1]
                        data = data[1:len(data)]
                        ALL_DATABASES[0].add(data)
                elif parsed_var[0] == "delete":
                    data = parsed_var[1]
                    ALL_DATABASES[0].delete(data)
                else:
                    print(
                        colored.red(f"{parsed_var[0]} is not defined")
                    )
                    break


                
