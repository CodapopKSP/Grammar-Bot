#Lists of Words
#Grammar Rules Functions
#Google Search Function

numberOfSentences = 10
sentence_nouns_probability = [1, 10, 40, 100, 95, 40, 10, 1]
sentence_verbs_probability = [100, 45, 1]
sentence_adjectives_probability = [75, 15, 1]


from random import randint
import nounlist, verblist, adjectivelist, determinerlist
from sentences import Statement
from utils import vowels

# Populate word lists
nouns = nounlist.nounsList
transitiveVerbs = verblist.transitiveVerbsList
intransitiveVerbs = verblist.intransitiveVerbsList
adjectives = adjectivelist.adjList
singularDeterminers = determinerlist.determinerSingularList
pluralDeterminers = determinerlist.determinerPluralList

def choose_word(percent_chance, word_list_type):
	percentRand = randint(0, 99)
	if percentRand < percent_chance:
		return word_list_type[randint(0, len(word_list_type)-1)]
	else:
		return ''

def choose_determiners(n):
	# Plural Determiners
	if n.pluralBool:
		determiner = pluralDeterminers[randint(0, len(pluralDeterminers)-1)]
		if n.duplicateBool:
			determiner = determiner + ' other'
	# Singular Determiners
	else:
		determiner = singularDeterminers[randint(0, len(singularDeterminers)-1)]
		if (determiner == 'a'):
			if len(n.adjList) > 0:
				if n.adjList[0].name[0] in vowels:
					determiner = 'an'
			else:
				if (n.pluralBool and (n.plural[0] in vowels)) or ((n.pluralBool == False) and n.singular[0] in vowels):
					determiner = 'an'
			if n.duplicateBool:
				determiner = 'another'
		else:
			if n.duplicateBool:
				determiner = determiner + ' other'
	# Finalize determiner
	n.add_determiner(determiner)


def main():

	sentence = Statement()


	# == Nouns ==
	# Select nouns
	for n in range(len(sentence_nouns_probability)):
		sentence.add_noun_to_sentence(choose_word(sentence_nouns_probability[n], nouns))

	# Randomly choose singular 0 or plural 1 for each noun, then choose adjectives
	for n in sentence.subjectNouns + sentence.objectNouns:
		pluralBool = randint(0, 1)
		n.decide_plural(pluralBool)
		for a in range(len(sentence_adjectives_probability)):
			n.add_adjectives(choose_word(sentence_adjectives_probability[a], adjectives))
		n.build_adjective_phrase()

	# Update the bool of each noun object that is duplicated in the sentence
	sentence.check_noun_duplicates()

	# Add determiners
	for n in sentence.subjectNouns + sentence.objectNouns:
		choose_determiners(n)

	# Build subject and object noun phrases
	for n in sentence.subjectNouns + sentence.objectNouns:
		n.build_noun_phrase()
	sentence.build_combo_noun_phrase()




	# == Verbs ==
	# Select verbs
	for v in range(len(sentence_verbs_probability)):
		if len(sentence.objectNouns) > 0:
			sentence.add_verb_to_sentence(choose_word(sentence_verbs_probability[v], transitiveVerbs))
		else:
			sentence.add_verb_to_sentence(choose_word(sentence_verbs_probability[v], intransitiveVerbs))
	# Decide verb tense and choose verb permutations accordingly
	tenseBool = randint(0, 1)
	for v in sentence.verbs:
		if tenseBool:
			v.permutation = v.past
		if (len(sentence.subjectNouns) < 2) and (sentence.subjectNouns[0].pluralBool == False):
			v.permutation = v.heSheIt
	sentence.check_verb_duplicates()
	sentence.build_verb_phrase()




	# Build final sentence and execute
	sentence.build_sentence()
	print(sentence.finalSentence)




for s in range(0, numberOfSentences):
	main()