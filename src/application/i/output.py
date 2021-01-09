from errors import Error

class Output():
	def __init__(self, data, var):
		self.data = data
		self.var = var
		self.is_valid_data()

	def is_valid_data(self):
		if self.data.startswith("[") and self.data.endswith("]"):
			data = self.data[1:len(self.data)]
			data = data[:-1]

			self.get_output(data)
		else:
			if self.data in self.var:
				self.get_output(self.var[self.data])
			else:
				er = Error(f"Name {self.data} not found")
				er.evoke()

	def get_output(self, data):
		print(data.replace("_", " "))