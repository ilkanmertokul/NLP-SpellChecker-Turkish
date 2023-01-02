import random

import nltk
from nltk import ngrams

from otherFunctions.helperFunctions import return_all_possible


class bigram:
    def __init__(self):
        self.wordMatrix = []
        self.countMatrix = []
        self.bitable = []
        self.ug = []
        self.total = 0


def bigram_runner(text):
    bi = bigram()
    bi.ug = list(ngrams(text, 2))

    print("\n\nYou started bigram.")
    get_bigram_class(bi)

    printmode = 0
    print("Calculating table. This takes really long time. You can enable printing to see where you are:\n"
          "1- go to bigram.py in ngram package\n"
          "2- modify line 29, second parameter to 0 -to-> 1 (printmode = 0 means no print)\n"
          f"current mode: {printmode}... \n")
    calculate_bigram_table(bi, printmode)

    return bi


##########################################################

def get_bigram_class(bigram):
    for token in bigram.ug:
        bigram.total += 1
        i = 0
        found = 0
        for word in bigram.wordMatrix:
            if token[0] == word:
                bigram.countMatrix[i] += 1
                found = 1
                break
            i += 1
        if found == 0:
            bigram.wordMatrix.append(token[0])
            bigram.countMatrix.append(1)
    print(f"Read total of {bigram.total} syllables")


#####################################################################################

def calculate_bigram_table(bigram, printmode):
    for i in range(0, len(bigram.wordMatrix)):
        e = []
        for j in range(0, len(bigram.wordMatrix)):
            e.append(0)
        bigram.bitable.append(e)
    #
    for i in range(0, len(bigram.wordMatrix)):
        for j in range(0, len(bigram.wordMatrix)):
            count = 0
            for k in range(0, len(bigram.ug)):
                if bigram.wordMatrix[i] == bigram.ug[k][0]:
                    count += 1
                if bigram.wordMatrix[i] == bigram.ug[k][0] and bigram.wordMatrix[j] == bigram.ug[k][1]:
                    if printmode:
                        print(
                            f"found i.{i} j.{j} k.{k}-> {bigram.wordMatrix[i]} == {bigram.ug[k][0]} and {bigram.wordMatrix[j]} == {bigram.ug[k][1]}")
                    bigram.bitable[i][j] += 1
            if bigram.bitable[i][j] == 0:
                bigram.bitable[i][j] = 0
            else:
                bigram.bitable[i][j] /= count
                if printmode:
                    print(bigram.bitable[i][j])


#####################################################################################

def get_best_bigram(sentence, bigram):
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
            for i in range(0, len(bigram.wordMatrix)):
                if bigram.wordMatrix[i][0] == token:
                    for j in range(0, len(bigram.wordMatrix)):
                        if bigram.wordMatrix[j][0] == token:
                            token_probability = bigram.bitable[i][j]
                            # print(f"found : {token}, with probability = {token_probability}")
            if token_probability == 0:
                token_probability = 0.9 / bigram.total
                # print(f"Could not find {token}, probability is {token_probability} according to laplace smoothing")

            probability *= token_probability

        if max == 1 or max < probability:
            most_possible = possible
            max = probability

    print(f"Most probable sentence is\n\"{most_possible}\"\nWith {max} probability!")
