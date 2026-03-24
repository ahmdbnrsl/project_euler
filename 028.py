current = 9
digits = [str(i) for i in range(1, 10)]
numbers = (9, '918273645')

while len(str(current)) < 9:
    str_pandigital = ""
    pengali = 1
    probability = True
    
    while len(str_pandigital) < 9 and probability:
        str_pandigital += str(current * pengali)
        if '0' in str_pandigital:
            probability = False
            break
        pengali += 1
    
    if not probability:
        current += 1
        continue
    pandigital = True
        
    for d in digits:
        if d not in str_pandigital:
            pandigital = False
            break
    
    if not pandigital or len(str_pandigital) > 9:
        current += 1
        continue
    numbers = (current, str_pandigital)
    print(numbers)
    current += 1

print(numbers)
    
    