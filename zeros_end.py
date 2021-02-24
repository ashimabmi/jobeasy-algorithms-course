
def zeros_end(number):
    while number % 10 == 0 and number != 0:
        number = number//10
    return number


print(zeros_end(14500))



















