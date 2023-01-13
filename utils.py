from enum import Enum

voicelessConsonants = ['s', 'x', 'z', 'h'] # h is for sh and ch
vowels = ['a', 'e', 'i', 'o', 'u']

class Quantity(Enum):
	SINGULAR = 1
	PLURAL = 2
	BOTH = 3