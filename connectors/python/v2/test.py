from pydob.db import PyDOB as Table

d = Table("hello")

d.set_fields(["name"])

d.add(["Pranav"])
