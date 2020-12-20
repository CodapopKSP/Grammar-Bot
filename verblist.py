from words import Verb

# Create verb objects in a list
transitiveVerbsList = []
intransitiveVerbsList = []
def add(present, irregular_past=None, irregular_past_participle=None, transitive=True):
	if transitive:
		transitiveVerbsList.append(Verb(present, irregular_past, irregular_past_participle, transitive))
	else:
		intransitiveVerbsList.append(Verb(present, irregular_past, irregular_past_participle, transitive))

# Regular Verbs
add('chase')
add('kill')
add('fuck')
add('destroy')
add('lick')
add('rub')
add('enjoy')
add('push')

# Irregular Verbs
add('eat', 'ate', 'eaten')
add('fight', 'fought')
add('hit', 'hit', 'hit')
add('bite', 'bit', 'bitten')

# Intransitive Verbs
add('cry', transitive=False)
add('play', transitive=False)