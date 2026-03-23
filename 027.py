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

def truncate_prime(n):
    is_prime = check_prime(n)
    if not is_prime: return False
    st = str(n)
    for i in range(len(st)-1):
        right, left = int(st[:i+1]), int(st[len(st)-i-1:])
        if not (check_prime(right) and check_prime(left)):
            return False
    return True

current_prime = 11
truncatable_prime = []

while len(truncatable_prime) < 11:
    tp = truncate_prime(current_prime)
    if tp: truncatable_prime.append(current_prime)
    current_prime = next_prime(current_prime)

summation = sum(truncatable_prime)
print(summation, truncatable_prime)