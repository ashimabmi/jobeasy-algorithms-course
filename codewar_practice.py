#Given your house number address and length of street n, give the house number on the opposite side of the street.

def over_the_road(address, n):
    odd_house = {}
    even_house = []
    j = 0

    for i in range(1, 2 * n + 1):
        print(i)
        if i % 2 != 0:
            odd_house[i] = j
            j = j + 1
        else:
            even_house.append(i)

    print(odd_house)
    decreasing_even = even_house[::-1]
    print(decreasing_even)
    return decreasing_even[odd_house.get(address)]


print(over_the_road(1, 3))
