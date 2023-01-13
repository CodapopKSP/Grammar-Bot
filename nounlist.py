from words import Noun

# Create noun objects in a list
nounsList = []
def add(singular, irregular_plural=None):
	nounsList.append(Noun(singular, irregular_plural))

# Regular Nouns
add('hero')
add('lady')
add('boy')
add('cat')
add('bird')
add('apple')
add('orange')
add('ear')
add('pencil')
add('eraser')
add('house')

# Irregular Nouns
add('mouse', 'mice')
add('deer', 'deer')
add('fish', 'fish')
add('person', 'people')
add('child', 'children')
add('goose', 'geese')
add('foot', 'feet')
add('man', 'men')
add('woman', 'women')