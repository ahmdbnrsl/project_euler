def check_prime(n):
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

def circular_prime(n):
    arr = list(str(n))
    
    for i in range(len(arr)):
        arr.append(arr[0])
        arr = arr[1:]
        if not check_prime(int("".join(arr))):
            return False
    return True

circulars = []
current_primes = 2

while current_primes <= 1_000_000:
    if current_primes in circulars:
        continue
    if circular_prime(current_primes):
        circulars.append(current_primes)
    current_primes = next_prime(current_primes)

print(circulars)
print(len(circulars))
    