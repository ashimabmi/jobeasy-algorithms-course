n = int(input('enter a number'))
n_arr = []
while n > 0:
    append_num = n % 10
    n = n//10
    n_arr.append(append_num)
result_arr = n_arr[::-1]
sum_digit = 0
for i in result_arr:
    sum_digit = sum_digit + i
print(sum_digit)
