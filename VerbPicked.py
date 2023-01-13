# Class for managing verbs picked
class Verb_Picked:
	def __init__(self, verb):
		self.present = verb.present
		self.past = verb.past()
		self.heSheIt = verb.he_she_it()
		self.permutation = verb.present