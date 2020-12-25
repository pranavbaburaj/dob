


class Strings():
    def __init__(self, pos, text):
        self.pos = pos
        self.text = text
        self.n_s = ""
        self.curr = self.set_curr()

    def set_curr(self):
        if len(self.text) == self.pos:
            return None
        else:
            return self.text[self.pos]

    def startEval(self):
        t_ = 0
        self.n_s = ""
        while self.curr is not None:
            t_ += 1
            self.pos += 1
            self.curr = self.set_curr()

            if self.curr == '"':
                break
            else:
                self.n_s += str(self.curr)

        # print(f"data={self.pos} str={self.n_s}")
        if len(self.n_s) == 1:
            type_ = "CHAR"
        else:
            type_ = "STR"
        return {
            "data" : self.n_s,
            "pos" : self.pos,
            "type" : type_
        }
