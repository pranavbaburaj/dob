from clint.textui import colored

class Error():
	def __init__(self, data):
		self.d = data

	def evoke(self):
		print(colored.red(self.d))

