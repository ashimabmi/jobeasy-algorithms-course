elements_li = [1, 2, 3, 4, 5, 0]
print('original list of elements', elements_li)


def below_arith_mean(elements):
    n = len(elements)
    s = 0
    for i in elements:
        s = s + i
    mean = s / n
    print('arithmetic mean:', mean)
    maximum = mean
    below_mean = []

    for i in range(n):
        if maximum > elements[i]:
            below_mean.append(elements[i])
    return 'list of elements below arithmetic mean:', below_mean


print(below_arith_mean(elements_li))




