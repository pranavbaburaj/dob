class TokenGenerator():
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"{self.type_}:{self.value}"