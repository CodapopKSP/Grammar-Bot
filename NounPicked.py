# Class for managing nouns and building phrases
class Noun_Picked:
	def __init__(self, noun):
		self.singular = noun.singular
		self.plural = noun.plural()
		self.name = noun.singular
		self.duplicateBool = False
		self.pluralBool = False
		self.adjList = []

	# Boolean to determine singular 0 or plural 1
	def decide_plural(self, plural_bool):
		self.pluralBool = plural_bool
		# Rename the word
		if plural_bool:
			self.name = self.plural

	# Choose adjectives
	def add_adjectives(self, adj=None):
		if adj:
			self.adjList.append(adj)

	# Build an adjective phrase, separating words with spaces, commas, and 'and' where necessary
	def build_adjective_phrase(self):
		self.check_adj_duplicates()
		if len(self.adjList) > 0:
			adjectivePhrase = self.adjList[0].name + ' '
			if len(self.adjList) > 1:
				adjectivePhrase = self.adjList[0].name + ', ' + self.adjList[1].name + ' '
				if len(self.adjList) > 2:
					adjectivePhrase = self.adjList[0].name + ', ' + self.adjList[1].name + ', and ' + self.adjList[2].name + ' '
			self.adjectivePhrase = adjectivePhrase
		else:
			self.adjectivePhrase = ''

	# Check for duplicate adjectives
	def check_adj_duplicates(self):
		adjDuplicateList = []
		for a in range(0, len(self.adjList)):
			for i in range(0, a):
				if (self.adjList[a].name == self.adjList[i].name):
					adjDuplicateList.append(a)
					break
		for i in range(0, len(adjDuplicateList)):
			self.adjList.pop(i)

	# Boolean to show if nouns list has this noun already
	def add_duplicate(self):
		self.duplicateBool = True

	# Add determiners with spaces
	def add_determiner(self, determiner):
		if determiner:
			self.determiner = determiner + ' '
		else:
			self.determiner = ''

	# Build the complete noun phrase
	def build_noun_phrase(self):
		self.nounPhrase = self.determiner + self.adjectivePhrase + self.name