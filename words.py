# Classes for all words

from utils import voicelessConsonants, vowels

# Noun class handles all noun permutations
class Noun:
	def __init__(self, singular, irregular_plural=None):
		self.singular = singular
		self.irregular_plural = irregular_plural

	def plural(self):
		plural = self.irregular_plural
		if self.irregular_plural == None:
			plural = self.singular + 's'
			if (self.singular[-1] in voicelessConsonants) or self.singular.endswith('o'):					# Issues with Italian words like 'piano'
				plural = self.singular + 'es'
			if self.singular.endswith('y') and (self.singular[-2] not in vowels):
					plural = self.singular[:-1]
					plural = plural + 'ies'
		return plural

	def singular_possessive(self):
		return self.singular + "'s"

	def plural_possessive(self):
		plural = self.irregular_plural
		if self.irregular_plural == None:
			plural = self.singular + 's'
			if (self.singular[-1] in voicelessConsonants) or self.singular.endswith('o'):					# Issues with Italian words like 'piano'
				plural = self.singular + 'es'
			if self.singular.endswith('y') and (self.singular[-2] not in vowels):
					plural = self.singular[:-1]
					plural = plural + 'ies'
			return plural + "'"
		else:
			return plural + "'s"




# Verb class handles all verb permutations
class Verb:
	def __init__(self, present, irregular_past=None, irregular_past_participle=None, transitive=True):
		self.present = present
		self.irregular_past = irregular_past
		self.irregular_past_participle = irregular_past_participle
		self.transitive = transitive

	def he_she_it(self):
		heSheIt = self.present + 's'
		if self.present[-1] in voicelessConsonants:
			heSheIt = self.present + 'es'
		if self.present.endswith('y') and (self.present[-2] not in vowels):
			heSheIt = self.present[:-1] + 'ies'
		return heSheIt

	def past(self):
		past = self.irregular_past
		if self.irregular_past == None:
			past = self.present + 'ed'
			if self.present.endswith('e'):
				past = self.present + 'd'
			if self.present.endswith('y') and (self.present[-2] not in vowels):
				past = self.present[:-1] + 'ied'
			if (self.present[-1] not in (vowels and 'y')) and (self.present[-2] in vowels) and (self.present[-3] not in vowels):
				past = self.present + self.present[-1] + 'ed'
		return past

	def past_participle(self):
		past_participle = self.irregular_past_participle
		if self.irregular_past_participle == None:
			past_participle = self.past()
		return past_participle

	def continuous(self):
		continuous = ''
		if self.present:
			continuous = self.present + 'ing'
			if self.present.endswith('e'):
				if self.present.endswith('ie'):
					continuous = self.present[:-2] + 'ying'
				else:
					continuous = self.present[:-1] + 'ing'
			if (self.present[-1] not in (vowels and 'y')) and (self.present[-2] in vowels) and (self.present[-3] not in vowels):
				continuous = self.present + self.present[-1] + 'ing'
		return continuous




# Adjective class handles adjectives and their opposites
class Adjective():
	def __init__(self, name, opposite=None):
		self.name = name
		self.opposite = opposite




# Adverb class handles adverbs and their opposites
class Adverb():
	def __init__(self, name, opposite=None):
		self.name = name
		self.opposite = opposite