# Enter a string of words separated by spaces. Find the longest word
input_words = input('enter string of words:')


def longest_word(word_li):
    if word_li is None:
        return 'this is not a valid input'
    words = word_li.split(' ')
    print(words)
    maximum = len(words[0])
    longest = words[0]
    for i in range(len(words)):
        print(len(words[i]))

        if not (maximum > len(words[i])):
            maximum = len(words[i])
            longest = words[i]

    return 'longest word is', longest


print(longest_word(input_words))
