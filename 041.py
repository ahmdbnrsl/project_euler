import math as m 

smallest = None
current_number = 100

while not smallest:
    limit = int(current_number * 10 / 6) + 1
    root_term = True
    for x in range(current_number, limit):
        ethnic = [i*x for i in range(1, 7)]
        initial_digit = str(ethnic[0])
        term = True
        for k in ethnic[1:]:
            if not term: break
            for j in str(k):
                if j not in initial_digit:
                    term = False
                    break
        if term:
            print(ethnic)
            root_term = False
            break
    if not root_term:
        break
    else: current_number *= 10