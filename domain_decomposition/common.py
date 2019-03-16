"""Module containing elements used by other submdules
"""

class Element():
	"""Class representing an element for spatial discitization

	Attributes
	----------
	_load_factor : double
		property discribing the computational cost of the element

	"""

	def __init__(self, load_factor = 1):
		self.load_factor = load_factor

	@property
	def load_factor(self):
		return self._load_factor

	@load_factor.setter
	def load_factor(self, value):
		if value < 0:
			raise ValueError("load_factor must be >= 0. Given <" + str(value) + ">")

		self._load_factor = value
	