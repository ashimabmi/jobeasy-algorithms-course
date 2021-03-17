elements_li = [10, 2, 3, 4, 5]
print('original list of elements', elements_li)


def lowest_two(elements, number_of_lowest):
    if number_of_lowest > len(elements):
        return elements
    sorted_elements = []
    for i in range(number_of_lowest):
        lowest = elements[0]
        for j in range(len(elements)):
            if elements[j] < lowest:
                lowest = elements[j]
        elements.remove(lowest)
        sorted_elements.append(lowest)
    return sorted_elements


print(lowest_two(elements_li, 2))
