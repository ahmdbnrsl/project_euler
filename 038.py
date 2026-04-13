def check_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def generate_dict_odd_squence_composite(n):
    squences = set()
    for i in range(2, 10):
        if not check_prime(i):
            squences.add(i)
        for k in range(2, n+1):
            squences.add(i * k)
    return sorted(squences)

n = 9999
dictionary = generate_dict_odd_squence_composite(n)
dictionary = [i for i in range(1000, 10000) if i not in dictionary]

for i in dictionary:
    squences = [i]
    squence = i + 3330
    next_squence = True
    for k in str(squence):
        if k not in str(i):
            next_squence = False
            break
    if next_squence and check_prime(squence):
        squences.append(squence)
        squence += 3330
        for k in str(squence):
            if k not in str(i):
                next_squence = False
                break
    
    if next_squence and check_prime(squence):
        squences.append(squence)
        print(squences)
    
    