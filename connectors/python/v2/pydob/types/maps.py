
class Maps(object):
	def __init__(self, data_types):
		self.data = self.get_data_types(data_types)
		self.maps = {}

	def get_data_types(self, data):
		if isinstance(data, tuple):
			return data[0:2]
		else:
			raise TypeError("Data type parameter should be a tuple")

	def add(self, i, v):
		if isinstance(i, self.data[0]) and isinstance(v, self.data[1]):
			if i not in self.maps:
				self.maps[i] = v
		else:
			raise TypeError("Data type not matching")

	def get(self):
		return self.maps

	def length(self):
		return len(self.maps)

	def keys(self):
		key = []
		for k in self.maps:
			key.append(k)
		return key

	def delete(self, key):
		if key in self.maps:
			del self.maps[key]
		
		return None

	def filter(self, value):
		arr = []

		for v in self.maps:
			if self.maps[v] == value:
				arr.append(v)

		return arr

	def clear(self):
		self.maps = {}
		return self.maps

	def change(self, i, v):
		if i in self.maps:
			if isinstance(v, self.data[1]):
				self.maps[i] = v