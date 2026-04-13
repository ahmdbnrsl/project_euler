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

current_prime = 2
sum_prime = 2

primes = [2]

while sum_prime <= 1000000:
    current_prime = next_prime(current_prime)
    sum_prime += current_prime
    primes.append(current_prime)

prime_sum = 0
true_sum = 0

for i in range(1, len(primes) + 1):
    prime_sum = sum(primes[:i])
    if check_prime(prime_sum):
        true_sum = prime_sum

print(true_sum)