import os
from clint.textui import colored as c

class FileReader():
    def __init__(self, file_name):
        self.file = file_name

    def read(self):
        data = ""
        try:
            with open(self.file, "r") as file_to_read:
                data = file_to_read.read()
        except:
            print(c.red(f"[{self.file}] : File not found"))
        return data.split("\n")
