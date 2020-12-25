import os, sys, platform

class OperatingSystemFunctions():
    @staticmethod
    def os_name():
        return platform.system()

    @staticmethod
    def node():
        return platform.uname().node

    @staticmethod
    def processor():
        return platform.processor()

    @staticmethod
    def location():
        return str(os.getcwd())