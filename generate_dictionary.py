def get_two_letter_list():
    import string
    characters = list(string.ascii_lowercase)
    two_letter_list = []
    for i in range(0, 10):
        for char in characters:
            two_letter_list.append(str(i) + char)
        for k in range(0, 10):
            two_letter_list.append(str(i) + str(k))

    for char in characters:
        for second_char in characters:
            two_letter_list.append(char + second_char)
        for k in range(0, 10):
            two_letter_list.append(char + str(k))
    return two_letter_list


def get_three_letter_list():
    import string, itertools
    characters = list(string.ascii_lowercase)
    combinations = itertools.combinations(characters, 3)
    letter_list = []

    for c in combinations:
        letter_list.append("" + c[0] + c[1] + c[2])

    return letter_list


def get_three_letter_list_with_digits():
    import string, itertools
    characters = list(string.ascii_lowercase)
    characters = characters + list(string.digits)
    combinations = itertools.combinations(characters, 3)
    letter_list = []

    for c in combinations:
        letter_list.append("" + c[0] + c[1] + c[2])

    return letter_list


def get_word_list(length_of_word):
    from hunspell import Hunspell
    from itertools import permutations
    import os
    import string
    hobj = Hunspell(os.path.join('/Users/Johannes/PycharmProjects/internetstiftelsen_domänkontroll/Swedish'),
                             os.path.join('/Users/Johannes/PycharmProjects/internetstiftelsen_domänkontroll/Swedish'))

    words = []
    for lst in permutations(sorted(string.ascii_lowercase), length_of_word):
        word = ''.join(lst)
        if word in words:
            continue
        if hobj.spell(word):
            words.append(word)
            #print(word)

    return words


def get_four_letter_word_list():
    return get_word_list(4)


def get_five_letter_word_list():
    return get_word_list(5)


if __name__ == '__main__':
    get_two_letter_list()
