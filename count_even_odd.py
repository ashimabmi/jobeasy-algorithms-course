number = int(input('enter a whole number:'))


def even_odd_digit(whole_number):
    digit_arr = []
    count_even = 0
    count_odd = 0
    i_arr_even = []
    i_arr_odd = []
    while whole_number > 0:
        digit = whole_number % 10
        whole_number = whole_number // 10
        digit_arr.append(digit)
    actual_digit = digit_arr[::-1]
    print(actual_digit)

    for i in actual_digit:
        if i % 2 == 0:
            count_even = count_even + 1
            i_arr_even.append(i)

        elif i % 2 != 0:
            count_odd = count_odd + 1
            i_arr_odd.append(i)

    print(f'even digits:{i_arr_even} and even count:{count_even}')
    print(f'odd digits:{i_arr_odd} and odd count:{count_odd}')


even_odd_digit(number)



