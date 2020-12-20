from words import Noun, Verb, Adjective, Adverb

vowels = ['a', 'e', 'i', 'o', 'u']


class Statement:
	def __init__(self):
		# Noun Assets
		self.subjectNouns = []
		self.objectNouns = []
		self.nounCount = 0

		# Verb Assets
		self.verbs = []

	def add_noun_to_sentence(self, noun=None):
		# Build subject and object nouns lists
		if self.nounCount < 4:
			if noun:
				nounPicked = Noun_Picked(noun.singular, noun.plural())
				self.subjectNouns.append(nounPicked)
		else:
			if noun:
				nounPicked = Noun_Picked(noun.singular, noun.plural())
				self.objectNouns.append(nounPicked)
		self.nounCount += 1

	def check_noun_duplicates(self):
		# Check for duplicates in subjectNouns and update bool
		for n in range(0, len(self.subjectNouns)):
			for i in range(0, n):
				if (self.subjectNouns[n].singular == self.subjectNouns[i].singular):
					self.subjectNouns[n].add_duplicate()

		# Check for duplicates in objectNouns and update bool
		for n in range(0, len(self.objectNouns)):
			for i in range(0, n):
				if self.objectNouns[n].singular == self.objectNouns[i].singular:
					self.objectNouns[n].add_duplicate()

		# Check for duplicates in objectNouns and subjectNouns and update bool
		for n in range(0, len(self.subjectNouns)):
			for i in range(0, len(self.objectNouns)):
				if self.subjectNouns[n].singular == self.objectNouns[i].singular:
					self.objectNouns[i].add_duplicate()

	def build_combo_noun_phrase(self):
		if len(self.subjectNouns) > 0:
			subjectPhrase = self.subjectNouns[0].nounPhrase + ' '
			if len(self.subjectNouns) > 1:
				subjectPhrase = self.subjectNouns[0].nounPhrase + ' and ' + self.subjectNouns[1].nounPhrase + ' '
				if len(self.subjectNouns) > 2:
					subjectPhrase = self.subjectNouns[0].nounPhrase + ', ' + self.subjectNouns[1].nounPhrase + ', and ' + self.subjectNouns[2].nounPhrase + ' '
					if len(self.subjectNouns) > 3:
						subjectPhrase = self.subjectNouns[0].nounPhrase + ', ' + self.subjectNouns[1].nounPhrase + ', ' + self.subjectNouns[2].nounPhrase + ', and ' + self.subjectNouns[3].nounPhrase + ' '
			self.subjectPhrase = subjectPhrase

		objectPhrase = ''
		if len(self.objectNouns) > 0:
			objectPhrase = self.objectNouns[0].nounPhrase
			if len(self.objectNouns) > 1:
				objectPhrase = self.objectNouns[0].nounPhrase + ' and ' + self.objectNouns[1].nounPhrase
				if len(self.objectNouns) > 2:
					objectPhrase = self.objectNouns[0].nounPhrase + ', ' + self.objectNouns[1].nounPhrase + ', and ' + self.objectNouns[2].nounPhrase
					if len(self.objectNouns) > 3:
						objectPhrase = self.objectNouns[0].nounPhrase + ', ' + self.objectNouns[1].nounPhrase + ', ' + self.objectNouns[2].nounPhrase + ', and ' + self.objectNouns[3].nounPhrase
		self.objectPhrase = objectPhrase

	def add_verb_to_sentence(self, verb=None):
		if verb:
			verbPicked = Verb_Picked(verb.present, verb.past(), verb.he_she_it())
			self.verbs.append(verbPicked)

	def check_verb_duplicates(self):
		# Check for duplicates in subjectNouns and update bool
		verbsDuplicateList = []
		for v in range(0, len(self.verbs)):
			for i in range(0, v):
				if (self.verbs[v].present == self.verbs[i].present):
					verbsDuplicateList.append(v)
					break
		for i in verbsDuplicateList:
			self.verbs.pop(i)

	def build_verb_phrase(self):
		if len(self.verbs) > 0:
			verbPhrase = self.verbs[0].permutation + ' '
			if len(self.verbs) > 1:
				verbPhrase = self.verbs[0].permutation + ' and ' + self.verbs[1].permutation + ' '
				if len(self.verbs) > 2:
					verbPhrase = self.verbs[0].permutation + ', ' + self.verbs[1].permutation + ', and ' + self.verbs[2].permutation + ' '
			self.verbPhrase = verbPhrase

	def build_sentence(self):
		if self.objectPhrase:
			finalSentence = self.subjectPhrase + self.verbPhrase + self.objectPhrase
		else:
			finalSentence = self.subjectPhrase + self.verbPhrase
		if finalSentence[-1] == ' ':
			finalSentence = finalSentence[:-1]
		self.finalSentence = finalSentence.capitalize() + '.'




class Noun_Picked:
	def __init__(self, singular, plural):
		self.singular = singular
		self.plural = plural
		self.name = singular
		self.duplicateBool = False
		self.pluralBool = False
		self.adjList = []

	# Boolean to determine singular 0 or plural 1
	def decide_plural(self, plural_bool):
		self.pluralBool = plural_bool
		if plural_bool:
			self.name = self.plural

	def add_adjectives(self, adj=None):
		if adj:
			self.adjList.append(adj)

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

	def add_determiner(self, determiner):
		if determiner:
			self.determiner = determiner + ' '
		else:
			self.determiner = ''

	def build_noun_phrase(self):
		self.nounPhrase = self.determiner + self.adjectivePhrase + self.name






class Verb_Picked:
	def __init__(self, present, past, he_she_it):
		self.present = present
		self.past = past
		self.heSheIt = he_she_it
		self.permutation = present