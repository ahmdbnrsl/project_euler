import math as m 

def generate_solution(n):
    solutions = []
    current_ab = []
    for i in range(1, int(n/2)):
        for j in range(1, int(n/2)):
            if i + j < n / 2 or i in current_ab or j in current_ab: continue
    
            a = i
            b = j
            c = m.sqrt(a * a + b * b)
            Terms = a % 1 + b % 1 + c % 1
            if not Terms and a + b + c == n:
                current_ab = [*current_ab, a, b]
                solutions.append((a, b, c))
    
    return solutions

current = (0, 0, [])
for i in range(1, 1000):
    print(i)
    sol = generate_solution(i)
    length = len(sol)
    if current[1] < length:
        current = (i, length, sol)

print(current)