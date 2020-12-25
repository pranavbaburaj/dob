NUMS = [
    str(number) for number in range(10)
]


class Numbers():
    def __init__(self, pos, text):
        self.pos = pos
        self.text = text
        self.num_str = ""
        self.curr = self.set_current_character()

    def set_current_character(self):
        if self.pos == len(self.text):
            return None
        else:
            return self.text[self.pos]


    def make_num(self):
        self.dots = 0

        while self.pos < len(self.text):
            if str(self.text[self.pos]) in NUMS or self.text[self.pos] == ".":
                self.num_str += str(self.text[self.pos])
            else:
                break
            self.pos += 1


        x = 0
        while x < len(self.num_str):
            if str(self.num_str[x]) == ".":
                if self.dots == 1:
                    break
                else:
                    self.dots += 1
                    break
            x += 1

        if self.dots > 0:
            self.t = "FLOAT"
        else:
            self.t = "INT"
        return self.pos, self.num_str, self.t
