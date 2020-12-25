import logging
import os
import json 
import uuid

class Database():
    def __init__(self):
        self.database = str(uuid.uuid4()).replace("-", "")[:8]
        self.create()
        self.dict_ = {}
        self.idx = 1
        self.all_fields = []

    def create(self):
        self.path = os.path.join(os.getcwd(), f"{self.database}.json")
        with open(self.path, "w") as file:
            file.write("")


    def fields(self, fields_):
        if self.all_fields:
            logging.error("Fields already set")
        else:
            for field in fields_:
                self.all_fields.append(field)

    def commit(self):
        with open(self.path, "w") as file:
            json.dump(self.dict_, file, indent=6)

    def add(self, c):
        self.dict_[str(self.idx)] = c
        self.idx += 1
        self.commit()

    def delete(self, i):
        if str(i) in self.dict_:
            del self.dict_[str(i)]
        self.commit()


