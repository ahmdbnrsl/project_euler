def check_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

current_counter = 0
current_multiplication = 0

for a in range(-999, 1000):
    for b in range(a, 1000):
        n = 0
        counter = 0
        while True:
            prime = check_prime(abs(n**2 + a*n + b))
            if not prime:
                break
            n += 1
            counter += 1
        
        if counter > current_counter:
            current_counter = counter
            current_multiplication = a * b
        
        if a != b:
            n_2 = 0
            counter_2 = 0
            
            while True:
                prime_2 = check_prime(abs(n_2**2 + b*n_2 + a))
                if not prime_2:
                    break
                
                n_2 += 1
                counter_2 += 1
        
            if counter_2 > current_counter:
                current_counter = counter_2
                current_multiplication = a * b
        
        print(current_counter, a, b, current_multiplication)

print(current_multiplication)