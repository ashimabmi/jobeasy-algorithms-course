#1.Convert number to reversed array of digits
def digitize(n):
    n_arr = []
    while n > 0:
        append_num = n % 10
        n = n//10
        n_arr.append(append_num)
    return n_arr


print(digitize(123456))

#2.Abbreviate a Two Word Name
#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.


def abbrev_name(name):
    if name is None:
        return 'this is not a valid input'
    name_split = name.split(' ')
    if len(name_split) != 2:
        return 'this is not a valid name'
    name_1 = name_split[0]

    name_2 = name_split[1]

    initials = name_1[0].upper() + '.' + name_2[0].upper()
    return initials


print(abbrev_name("Avi Sha"))
