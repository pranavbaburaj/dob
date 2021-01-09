from errors import Error

class Variable:
	def __init__(self, data, var):
		self.data = data
		self.var = var

		self.start()

	def start(self):
		numbers = [str(x) for x in range(10)]
		if self.data[0] in numbers:
			d_er = Error("Variable name cannot start with a number")
			d_er.evoke()
		else:
			if ":" in self.data:
				data = self.data.split(":")
				self.var[str(data[0])] = data[1]
			else:
				self.var[str(self.data)] = "Hello_World"