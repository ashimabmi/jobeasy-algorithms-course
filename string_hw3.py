input_word = 'Ashima'


def count(input_words):
    words = {}
    for item in input_words.lower():
        if item in words:
            words[item] = words[item] + 1
        else:
            words[item] = 1

    for key, value in words.items():
        return words


print(count(input_word))
