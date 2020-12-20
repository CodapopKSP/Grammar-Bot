# Add all nouns' possessives

# Create determiner objects in lists
determinerSingularList = []
determinerPluralList = []

def add(name, singular=None, plural=None):
	if singular:
		determinerSingularList.append(name)
	if plural:
		determinerPluralList.append(name)

# Singular-Only Determiners
add('a', True)
add('this', True)
add('that', True)
add('each', True)
add('every', True)

# Plural-Only Determiners
add('', False, True)
add('these', False, True)
add('those', False, True)
add('some', False, True)
add('many', False, True)
add('all', False, True)
add('most', False, True)
add('several', False, True)
add('almost all', False, True)
add('no', False, True)
add('a few', False, True)

add('a lot of', False, True)
add('a pair of', False, True)
add('plenty of', False, True)
add('a great deal of', False, True)
add('a couple of', False, True)
add('a number of', False, True)

add('none of the', False, True)
add('almost none of the', False, True)
add('some of the', False, True)
add('many of the', False, True)
add('all of the', False, True)
add('a few of the', False, True)
add('a couple of the', False, True)
add('most of the', False, True)
add('a number of the', False, True)
add('a great deal of the', False, True)
add('a pair of the', False, True)
add('a lot of the', False, True)


# Both Determiners
add('the', True, True)

add('my', True, True)
add('your', True, True)
add('his', True, True)
add('her', True, True)
add('its', True, True)
add('our', True, True)
add('their', True, True)