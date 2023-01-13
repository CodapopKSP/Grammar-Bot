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
add('energetic', 'sleepy')
add('expensive', 'cheap')
add('excited', 'bored')
add('rich', 'poor')
add('intelligent', 'stupid')
add('normal', 'crazy')
add('black', 'white')

add('small', 'big')
add('cold', 'hot')
add('thin', 'fat')
add('sad', 'happy')
add('short', 'tall')
add('ugly', 'beautiful')
add('stinky', 'fragrant')
add('bald', 'hairy')
add('sleepy', 'energetic')
add('cheap', 'expensive')
add('bored', 'excited')
add('poor', 'rich')
add('stupid', 'intelligent')
add('crazy', 'normal')
add('white', 'black')


add('red')
add('blue')