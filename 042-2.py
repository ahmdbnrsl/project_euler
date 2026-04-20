import sys
import math as m 

sys.set_int_max_str_digits(2147483647)

one_hundred_factorial = [i for i in range(1, 101)]

count = 0

for n in range(1, 101):
    for r in range(1, 101):
        if r > n: continue
        term = m.prod(one_hundred_factorial[:n][r:]) / m.prod(one_hundred_factorial[:n - r])
        if term > 1_000_000:
            print(term)
            count += 1

print(count)