import math as m 

def get_digit_irrational(*request):
    capacity_digit = 9
    pack_digit = 1
    prev_digit = 0
    prev_number = 0
    digits = []
    numbers = []
    
    for n in request:
        while n > capacity_digit:
            prev_number += 9 * 10 ** (pack_digit - 1)
            prev_digit = capacity_digit
            pack_digit += 1
            capacity_digit += 9 * 10 ** (pack_digit - 1) * pack_digit
        
        difference = (n - prev_digit) / pack_digit
        modulo = round((difference - int(difference)) * pack_digit)
        index = modulo - 1 if modulo > 0 else pack_digit - 1
        number = prev_number + m.ceil(difference)
        digit = str(number)[index]
        
        numbers.append(number)
        digits.append(int(digit))
    
    return digits, numbers


print(get_digit_irrational(4, 16, 127, 211, 216, 320, 610))
print(get_digit_irrational(1, 10, 100, 1000, 10000, 100000, 1000000, 1000000000))
print(get_digit_irrational(1000000, 1000001, 1000002, 1000003, 1000004, 1000005))