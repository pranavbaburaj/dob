import flasking as f
from flask import Flask

app = Flask(__name__)

d = f.RollerDB("hello", app)

d.set_fields(["name", "age", "class"])


print(d.fields)