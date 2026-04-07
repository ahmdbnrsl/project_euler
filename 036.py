def check_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

christian_goldbach = None
current_composite_number = 9

while not christian_goldbach:
    if not check_prime(current_composite_number) :
        is_christian_goldbach = False
        current_quadrat = 1
        
        while current_composite_number - 2 * current_quadrat ** 2 >= 2:
            if check_prime(current_composite_number - 2 * current_quadrat ** 2):
                is_christian_goldbach = True
                break
            current_quadrat += 1
        
        if not is_christian_goldbach:
            christian_goldbach = current_composite_number
            break
    current_composite_number += 2

print(christian_goldbach)