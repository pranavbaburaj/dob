import platform
import uuid

APPLICATION_NAME = "DoB"
APPLICATION_VERSION = "1.0.0"
AUTHORS = [
    "P Pranav Baburaj"
]

DEPENDENCIES = [
    "PyQt5",
    "clint"
]

PLATFORM_NAME = [
    platform.system()  
]

DATABASE_NAME = str(uuid.uuid4()).replace("-", "_")[:8]
