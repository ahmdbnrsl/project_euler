def fibonacci(n):
    n_2 = 0
    n_1 = 1
    if n == 0:
        return n_2
    elif n == 1:
        return n_1
    else:
        for i in range(2, n + 1):
            n_2, n_1 = n_1, n_2 + n_1
        return n_1

counter = 4500
while True:
    f = fibonacci(counter)
    if len(str(f)) == 1000:
        print(counter)
        break
    counter += 1

print(len(str(fibonacci(4781))))