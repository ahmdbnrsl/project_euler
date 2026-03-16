def division(n, d):
    if d == 0: return str(None)
    if n % d == 0: return str(0)
    
    arr = []
    mods = []
    
    while n != 0 and len(arr) <= 4000:
        while n < d:
            n *= 10
            if n < d: arr.append(0)

        mod = n % d
        divide = int(n / d)
        tup = (mod, divide)
        
        if tup in mods:
            break
        
        mods.append(tup)
        arr.append(divide)
        
        n = mod
    
    return "".join(str(i) for i in arr)

current = (0, 0, "")
for i in range(1, 1000):
    pgpt = division(1, i)
    length = len(pgpt)
    if current[1] < length:
        current = (i, length, pgpt)

print(current)