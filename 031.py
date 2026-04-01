import math as m
import itertools

def check_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

pandigitals = [str(i) for i in range(1, 10)]

count = 1

while len(pandigitals) > 1:
    found = False
    pandigitals.reverse()
    for i in itertools.permutations(pandigitals):
        number = int("".join(i))
        if check_prime(number):
            print(number)
            found = True
            break
    
    if found:
        break
    else:
        pandigitals.reverse()
        pandigitals = pandigitals[:-1]
    