input_irregular = input('enter string of words:')


def regular(irregular):
    return " ".join(irregular.strip(" ").split())


print(regular(input_irregular))
