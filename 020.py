import math as m

current_square = 1
n_by_n = 1
diagonal_sum = 1

while n_by_n < 1001:
    latest = int(m.sqrt(current_square))
    temp_square = (latest + 2)**2
    
    for i in range(temp_square, current_square, -(latest + 1)):
        diagonal_sum += i
    
    current_square = temp_square
    n_by_n += 2

print(diagonal_sum)