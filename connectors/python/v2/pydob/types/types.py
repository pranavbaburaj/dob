from pydob.types import List
from pydob.types import Maps

class Types:
    # integers and floats are
    # considered as numbers
    @staticmethod
    def numbers():
        return [int, float]

    @staticmethod
    def text():
        return [str]

    @staticmethod
    def lists():
        return [List]

    @staticmethod
    def maps():
        return [Maps]


