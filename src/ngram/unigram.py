import nltk
from nltk import ngrams
import nltk

from otherFunctions.helperFunctions import return_all_possible

debugMode = 0


class unigram:
    def __init__(self):
        self.wordMatrix = []
        self.countMatrix = []
        self.unigramtable = []
        self.ug = []
        self.total = 0
        self.oneCount = 0


def unigram_runner(text):
    u = unigram()
    u.ug = ngrams(text, 1)

    print("You started unigram!")
    get_unigram_class(text, u)

    print("\nCalculating unigrams")
    calculate_unigram_table(u)

    if debugMode:
        for i in range(0, len(u.unigramtable)):
            print(f"{u.wordMatrix[i]}, {u.countMatrix[i]}")

    return u


###############################

def get_best(sentence,unigram):

    possibles = return_all_possible(sentence)
    print(f"\nFound total of {len(possibles)} combinations of = - {sentence} -\nHere are a few:")
    i = 0
    for possible in possibles:
        if i > 3:
            break
        else:
            print(possible)
            i += 1

    print("\nCalculating the most highly version...\n")
    max = 1;
    most_possible = ""

    for possible in possibles:
        # Tokenizes words
        tokens = nltk.word_tokenize(possible)
        probability = 1
        for token in tokens:
            token_probability = 0
            for i in range(0,len(unigram.unigramtable)):
                if unigram.wordMatrix[i][0] == token:
                    token_probability = unigram.unigramtable[i]
                    #print(f"found : {token}, with probability = {token_probability}")
            if token_probability == 0:
                token_probability = 0.9 / unigram.total
                #print(f"Could not find {token}, probability is {token_probability} according to laplace smoothing")

            probability *= token_probability

        if max == 1 or max < probability:
            most_possible = possible
            max = probability

    print(f"Most probable sentence is\n\"{most_possible}\"\nWith {max} probability!")


###############################

def get_unigram_class(text, u):
    # get ALL
    for token in u.ug:
        u.total += 1
        i = 0
        found = 0
        for word in u.wordMatrix:
            if token == word:
                u.countMatrix[i] += 1
                found = 1
                break
            i += 1
        if found == 0:
            u.wordMatrix.append(token)
            u.countMatrix.append(1)
    print(f"Read total of {u.total} words!")


def calculate_unigram_table(unig):
    # now it is time to unigram table.
    for i in unig.countMatrix:
        if i == 1:
            unig.oneCount +=1

    for i in unig.countMatrix:
            unig.unigramtable.append(i / unig.total)
