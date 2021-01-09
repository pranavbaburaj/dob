from output import Output
from errors import Error
from variables import Variable

ALL_ID = [
	"-o", "-v", "-t"
]

variables = {
	
}

class IdObject:
	def __init__(self, data, pos):
		self.data = data
		self.pos = pos + 1
		self.get_id()

	def curr(self):
		if self.pos == len(self.data):
			return None
		else:
			return self.data[self.pos]
	def condition(self):
		if self.pos + 1 == len(self.data):
			return False
		else:
			return True

	def get_id(self):
		self.c = self.curr()
		while self.c is not None:
			line_ended = False
			if self.c == ";":
				line_ended = True
				break
			elif self.c in ALL_ID:
				if self.c == "-o":
					if self.pos + 1 == len(self.data):
						print("\n")
					else:
						out = Output(self.data[self.pos + 1], variables)
				elif self.c == "-v":
					if self.condition():
						index_data = self.data[self.pos + 1]
						if index_data == "" or index_data == " ":
							der = Error("Variable declaration failed").evoke()
						else:
							var_ = Variable(index_data, variables)
					else:
						der = Error("Variable declaration failed").evoke()

			self.pos += 1
			self.c = self.curr()


	
