numerators = []
denumerators = []

for i in range(10, 100):
    for j in range(i+1, 100):
        if i >= 99: break
        numerator = [*list(str(i))]
        denumerator = [*list(str(j))]
        
        for k in denumerator:
            if k in numerator and int(k) != 0:
                numerator.remove(k)
                denumerator.remove(k)
                break
        
        if int(denumerator[0]) == 0 or len(numerator) > 1: continue
        if int(numerator[0]) / int(denumerator[0]) == i / j:
            print(int(numerator[0]) , int(denumerator[0]), i, j)
            numerators.append(i)
            denumerators.append(j)

import math as m
print(m.prod(numerators), m.prod(denumerators))