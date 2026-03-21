import math as m

numbers = 0
n = 3

while True:
    sum_digit = 0
    for d in str(n):
        sum_digit += m.factorial(int(d))
    if sum_digit == n:
        numbers += n
        print(numbers)
    n += 1