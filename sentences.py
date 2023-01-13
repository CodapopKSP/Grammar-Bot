# |--------------|
# |  Statements  |
# |--------------|

from NounPicked import Noun_Picked
from VerbPicked import Verb_Picked

# Builds a sentence by choosing parts of speech and combining them
class Statement:
	def __init__(self):
		# Noun Assets
		self.subjectNouns = []
		self.objectNouns = []
		self.nounCount = 0

		# Verb Assets
		self.verbs = []

	# Choose nouns and add them to subject or object lists
	def add_noun_to_sentence(self, noun=None):
		# Subject nouns
		if self.nounCount < 4:
			if noun:
				nounPicked = Noun_Picked(noun)
				self.subjectNouns.append(nounPicked)
		# Object nouns
		else:
			if noun:
				nounPicked = Noun_Picked(noun)
				self.objectNouns.append(nounPicked)
		self.nounCount += 1

	# Check for duplicates in subject and object nouns lists
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

	# Build a noun phrases, separating words with spaces, commas, and 'and' where necessary
	def build_combo_noun_phrase(self):
		#Subject nouns
		if len(self.subjectNouns) > 0:
			subjectPhrase = self.subjectNouns[0].nounPhrase + ' '
			if len(self.subjectNouns) > 1:
				subjectPhrase = self.subjectNouns[0].nounPhrase + ' and ' + self.subjectNouns[1].nounPhrase + ' '
				if len(self.subjectNouns) > 2:
					subjectPhrase = self.subjectNouns[0].nounPhrase + ', ' + self.subjectNouns[1].nounPhrase + ', and ' + self.subjectNouns[2].nounPhrase + ' '
					if len(self.subjectNouns) > 3:
						subjectPhrase = self.subjectNouns[0].nounPhrase + ', ' + self.subjectNouns[1].nounPhrase + ', ' + self.subjectNouns[2].nounPhrase + ', and ' + self.subjectNouns[3].nounPhrase + ' '
			self.subjectPhrase = subjectPhrase
		# Object nouns
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

	# Add verbs to list to prepare for phrase building
	def add_verb_to_sentence(self, verb=None):
		if verb:
			verbPicked = Verb_Picked(verb)
			self.verbs.append(verbPicked)

	# Make sure there are no duplicate verbs
	def check_verb_duplicates(self):
		verbsDuplicateList = []
		for v in range(0, len(self.verbs)):
			for i in range(0, v):
				if (self.verbs[v].present == self.verbs[i].present):
					verbsDuplicateList.append(v)
					break
		for i in verbsDuplicateList:
			self.verbs.pop(i)

	# Build a verb phrases, separating words with spaces, commas, and 'and' where necessary
	def build_verb_phrase(self):
		if len(self.verbs) > 0:
			verbPhrase = self.verbs[0].permutation + ' '
			if len(self.verbs) > 1:
				verbPhrase = self.verbs[0].permutation + ' and ' + self.verbs[1].permutation + ' '
				if len(self.verbs) > 2:
					verbPhrase = self.verbs[0].permutation + ', ' + self.verbs[1].permutation + ', and ' + self.verbs[2].permutation + ' '
			self.verbPhrase = verbPhrase

	# Build the final sentence with punctuation
	def build_sentence(self):
		if self.objectPhrase:
			finalSentence = self.subjectPhrase + self.verbPhrase + self.objectPhrase
		else:
			finalSentence = self.subjectPhrase + self.verbPhrase
		if finalSentence[-1] == ' ':
			finalSentence = finalSentence[:-1]
		self.finalSentence = finalSentence.capitalize() + '.'