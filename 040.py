import itertools as it

def check_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

perms = set()
current_digits = []

for i in it.permutations(["*", "*", "*", "_", "_"]):
    perms.add("".join(list(i)))

permutations = [list(i) for i in perms]

for i in permutations:
    last_digit = [i for i in range(1, 10) if i % 2 != 0 or i % 5 != 0]
    for k in last_digit:
        r = [*i, k]
        indexs_underscore = [l for l, e in enumerate(i) if e == "_"]
        indexs_asterisk = [l for l, e in enumerate(i) if e == "*"]
        start_first_digit = 0
        if i[0] == "_": start_first_digit = 1
        for m in range(start_first_digit, 10):
            for n in range(0, 10):
                if (m + n + k) % 3 == 0: continue
                digits = []
                for a in range(1, 10):
                    digit = [0 for _ in range(5)]
                    for b in indexs_asterisk:
                        digit[b] = str(a)
                    for idc, b in enumerate(indexs_underscore):
                        digit[b] = str([m, n][idc])
                    digit.append(str(k))
                    print(digit, indexs_underscore, indexs_asterisk)
                    number = int(''.join(digit))
                    if check_prime(number):
                        digits.append(number)
                if len(digits) == 8: current_digits = digits

print(current_digits)