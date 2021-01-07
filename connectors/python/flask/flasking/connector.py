import flask
import os
import json
from flask import views
from flask import redirect

all_databases = []

class AdminPanel():
    def get(self):
        return all_databases[0].dictionary

    def post(self):
        return "POST not supported"


class RollerDB():
    def __init__(self, name, flask_app):
        self.name = name
        self.app = flask_app
        self.add_installed_application()
        self.dictionary = {}
        self.idx = 1
        self.file_path = self.get_path()
        self.fields = []
        self.create()

    def add_installed_application(self):
        all_databases.append(self.app)

    def commit(self):
        if self.is_valid_app():
            with open(self.file_path, "w") as file_:
                json.dump(self.dictionary, file_, indent=6)
        else:
            raise TypeError("App not a Flask app")

    def admin(self, url):
        self.app.add_url_rule(url, view_func=AdminPanel.as_views("admin"))

    def create(self):
        self.commit()
        return True

    def is_valid_app(self):
        return isinstance(self.app, flask.app.Flask)

    def get_path(self):
        return f"{self.name}.json" 

    def add(self, data_to_add):
        if isinstance(data_to_add, list):
            dict_value = {}
            for x in range(len(self.fields)):
                dict_value[self.fields[x]] = data_to_add[x]
            self.dictionary[str(self.idx)] = dict_value
            self.idx += 1
            self.commit()
        else:
            raise TypeError("Data should be in list form")

    def all(self):
        return self.dictionary

    def set_fields(self, f):
        if self.fields:
            raise Exception("Fields are already set")
        else:
            if isinstance(f, list):
                for i in range(len(f)):
                    if f[i] not in self.fields:
                        self.fields.append(f[i])
            else:
                raise TypeError("Fields need to be lists")

    