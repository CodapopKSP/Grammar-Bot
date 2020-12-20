from words import Adjective

# Create adjective objects in a list
adjList = []
def add(name, opposite=None):
	adjList.append(Adjective(name, opposite))

# Adjectives
add('big', 'small')
add('hot', 'cold')
add('fat', 'thin')
add('happy', 'sad')
add('tall', 'short')
add('beautiful', 'ugly')
add('fragrant', 'stinky')
add('hairy', 'bald')