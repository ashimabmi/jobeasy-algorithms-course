
def recursive_sum(number):
    n_arr = []
    while number >= 1:
        remainder = number % 10
        number = number//10
        n_arr.append(remainder)
    result_arr = n_arr[::-1]
    sum_digit = 0
    for i in result_arr:
        sum_digit = sum_digit + i

    if len(str(sum_digit)) > 1:

        return recursive_sum(sum_digit)
    else:
        return sum_digit


print(recursive_sum(132189))




