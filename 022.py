def sum_pandigital(m, n, o, p):
    pandigitals = set()
    digits = [str(i) for i in range(1, 10)]
    
    for i in range(m, n):
        for j in range(o, p):
            this_digit = [
                *list(str(i)),
                *list(str(j)),
                *list(str(i * j))]
            
            pandigital = True
            
            for d in digits:
                if d not in this_digit:
                    pandigital = False
                    break
            
            if not pandigital or len(this_digit) > 9: continue
            pandigitals.add(i * j)
            
    return sum(pandigitals)

print(sum_pandigital(1000, 10000, 1, 10) + sum_pandigital(100, 1000, 10, 100))