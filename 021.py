
numbers = 4151
list_numbers = [4150]

while True:
    su = sum(int(i)**5 for i in str(numbers))
    if numbers > 1 and numbers == su:
        list_numbers.append(numbers)
        print(numbers, sum(list_numbers))
    numbers += 1