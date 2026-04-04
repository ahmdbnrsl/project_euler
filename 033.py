import itertools as it

pandigitals = [str(i) for i in range(10)]
primes = [2, 3, 5, 7, 11, 13, 17]
sums = 0

for pandigital in it.permutations(pandigitals):
    if pandigital[0] != "0":
        terms = True
        for i, prime in zip(range(len(pandigital) - 3), primes):
            string = pandigital[i+1] + pandigital[i+2] + pandigital[i+3]
            integer = int(string)
            if integer % prime != 0:
                terms = False
                break
        
        if terms:
            sums += int("".join(pandigital))

print(sums)