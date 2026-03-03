import math as m

def lattice_paths(n):
    f = lambda number: m.prod(i for i in range(1, number + 1))
    c = lambda n, r: f(n) / (f(n - r) * f(r))
    result = sum((c(n, r))**2 for r in range(n-1, 0, -1))
    
    return result + 2

print(lattice_paths(20))