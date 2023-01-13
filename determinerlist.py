# Add all nouns' possessives

from utils import Quantity

# Create determiner objects in lists
determinerSingularList = []
determinerPluralList = []

def add(name, quantity):
	if quantity == Quantity.SINGULAR or quantity == Quantity.BOTH:
		determinerSingularList.append(name)
	if quantity == Quantity.PLURAL or quantity == Quantity.BOTH:
		determinerPluralList.append(name)

# Singular-Only Determiners
add('a', Quantity.SINGULAR)
add('this', Quantity.SINGULAR)
add('that', Quantity.SINGULAR)
add('each', Quantity.SINGULAR)
add('every', Quantity.SINGULAR)

# Plural-Only Determiners
add('', Quantity.PLURAL)
add('these', Quantity.PLURAL)
add('those', Quantity.PLURAL)
add('some', Quantity.PLURAL)
add('many', Quantity.PLURAL)
add('all', Quantity.PLURAL)
add('most', Quantity.PLURAL)
add('several', Quantity.PLURAL)
add('almost all', Quantity.PLURAL)
add('no', Quantity.PLURAL)
add('a few', Quantity.PLURAL)

add('a lot of', Quantity.PLURAL)
add('a pair of', Quantity.PLURAL)
add('plenty of', Quantity.PLURAL)
add('a great deal of', Quantity.PLURAL)
add('a couple of', Quantity.PLURAL)
add('a number of', Quantity.PLURAL)

add('none of the', Quantity.PLURAL)
add('almost none of the', Quantity.PLURAL)
add('some of the', Quantity.PLURAL)
add('many of the', Quantity.PLURAL)
add('all of the', Quantity.PLURAL)
add('a few of the', Quantity.PLURAL)
add('a couple of the', Quantity.PLURAL)
add('most of the', Quantity.PLURAL)
add('a number of the', Quantity.PLURAL)
add('a great deal of the', Quantity.PLURAL)
add('a pair of the', Quantity.PLURAL)
add('a lot of the', Quantity.PLURAL)


# Both Determiners
add('the', Quantity.BOTH)

add('my', Quantity.BOTH)
add('your', Quantity.BOTH)
add('his', Quantity.BOTH)
add('her', Quantity.BOTH)
add('its', Quantity.BOTH)
add('our', Quantity.BOTH)
add('their', Quantity.BOTH)