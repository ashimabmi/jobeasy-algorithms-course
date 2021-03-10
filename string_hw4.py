sentence = input('enter a sentence:')
sub_1 = input('enter sub string:')
sub_2 = input('enter the sub string to replace')


def replace(s, s1, s2):
    ind_1 = sentence.index(sub_1)
    print(ind_1)

    for i in range(len(s2)):
        s[ind_1 + i] = s2[i]

    return "".join(s)


print(replace(list(sentence), list(sub_1), list(sub_2)))
