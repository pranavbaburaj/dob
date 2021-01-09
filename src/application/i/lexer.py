from errors import Error
from id import IdObject

ID = ":"

class Lexer:
	def __init__(self, data):
		self.data = data.split(" ")
		self.pos  = 0
		self.tokens = []

	def set_current_character(self):
		if self.pos == len(self.data):
			return None
		else:
			return self.data[self.pos]

	def start_evaluation(self):
		self.curr = self.set_current_character()
		line_ended = False

		while self.curr is not None:
			if self.curr == ";":
				line_ended = True
				break
			elif self.curr == ID:
				new_id = IdObject(self.data, self.pos)
			elif self.curr == "#":
				if not line_ended:
					error = Error("Cannot include comment before ending the line")
					error.evoke()
				break

			self.pos += 1
			self.curr = self.set_current_character()

		return self.tokens
			
