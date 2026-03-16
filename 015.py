import math as m

def amicable(x, y):
    x_set = set()
    y_set = set()
    
    for i in range(1, int(m.sqrt(x)) + 1):
        if x % i != 0: continue
        x_set.update([i, int(x / i)])
    for i in range(1, int(m.sqrt(y)) + 1):
        if y % i != 0: continue
        y_set.update([i, int(y / i)])
    
    sum_x_divisors = sum(x_set) - x
    sum_y_divisors = sum(y_set) - y
    
    total = sum_x_divisors + sum_y_divisors
    return x != y and sum_x_divisors == y and sum_y_divisors == x, sum_x_divisors, sum_y_divisors

def check_prime(number: int) -> bool:
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

def generate_dict_prime() -> list[int]:
    result = [2]
    current_number = 2
    limit = 10**11
    
    while current_number * current_number <= limit:
        current_number += 1
        while not check_prime(current_number):
            current_number += 1
        result.append(current_number)
    return result

counter = 0
# primes = generate_dict_prime()
print("Primes Dict Already Generated")

for i in range(0, 10000):
    for j in range(i, 10000):
        if i == j: continue
        condition, sum_x, sum_y = amicable(i, j)
        if condition:
            counter += sum_x + sum_y
            print(counter)

print(counter)
print(amicable(220, 284))