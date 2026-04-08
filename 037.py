def check_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def next_prime(n):
    np = n + 1
    while not check_prime(np):
        np += 1
    return np

def unique_factorization(n):
    prime = 2
    if n <= prime: return [n]
    factors = []

    while not check_prime(n):
        if n % prime == 0:
            n = n / prime
            factors.append(prime)
        else:
            prime = next_prime(prime)

    factors.append(n)
    return set(factors)


def generate_dict_odd_squence_composite(n):
    squences = set()
    for i in range(2, 10):
        if not check_prime(i):
            squences.add(i)
        for k in range(2, n+1):
            squences.add(i * k)
    return sorted(squences)

n = 150000
dictionary = generate_dict_odd_squence_composite(n)

current_index = 0
consecutive_dictionary = []
while current_index < n - 1:
    consecutive_numbers = set()
    current_element = dictionary[current_index]
    consecutive_numbers.add(current_element)
    
    while current_element + 1 == dictionary[current_index + 1]:
        
        current_index += 1
        current_element = dictionary[current_index]
        consecutive_numbers.add(current_element)
    
    consecutive_dictionary.append(consecutive_numbers)
    current_index += 1

above_four_consecutives = [i for i in consecutive_dictionary if len(i) >= 4]

for i in above_four_consecutives:
    group = []
    factors = []
    numbers = set()
    for k in i:
        factor = unique_factorization(k)
        if len(factor) == 4:
            factors.append(factor)
            numbers.add(k)
        else:
            group.append((factors, numbers))
            factors = []
            numbers = set()
    
    if len(factors) > 0 and len(numbers) > 0:
        group.append((factors, numbers))
    
    for k in group:
        if len(k[1]) == 4:
            print(k)
            break

# consecutives = []

# for i in range(100000, 200000):
#     factor = set(unique_factorization(i))
#     if len(factor) == 4:
#         consecutives.append(i)

# index = 0
# ccons_arr = []

# while index < len(consecutives):
#     arr = []
#     if index + 1 >= len(consecutives) - 1:
#         break
    
#     while consecutives[index + 1] - consecutives[index] == 1:
#         arr = [*arr, consecutives[index], consecutives[index + 1]]
#         index += 1
    
#     ccons_arr.append(set(arr))
#     index += 1

# for i in ccons_arr:
#     if len(i) > 0:
#         print(i)