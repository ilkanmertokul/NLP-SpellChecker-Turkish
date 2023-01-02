def smaller(oldText):
    return oldText.lower()


def return_all_possible(word):
    rules = [['ı', 'i'], ['u', 'ü'], ['o', 'ö'], ['ğ', 'g'], ['s', 'ş'], ['c', 'ç']]
    possibles = []
    return_all_possibles(word, rules, 0, possibles)
    return possibles


def return_all_possibles(word, rules, index, possibles):
    if index == len(word):
        possibles.append(word)
        return

    for rule in rules:
        if word[index] == rule[0] or word[index] == rule[1]:
            return_all_possibles(word[:index] + rule[0] + word[index + 1:], rules, index + 1, possibles)
            return_all_possibles(word[:index] + rule[1] + word[index + 1:], rules, index + 1, possibles)
            return

    return_all_possibles(word, rules, index + 1, possibles)
