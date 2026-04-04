dictionary = [chr(i) for i in range(65, 91)]
dictionary_squences = [(1/2)*n*(n + 1) for n in range(1, 10001)]

with open('0042_words.txt', 'r') as file:
    content = file.read()
    list_of_contents = content.split('","')
    splitted = list_of_contents[1:-1]
    a, b = list(list_of_contents[0]), list(list_of_contents[-1])
    
    a.remove('"')
    b.remove('"')
    
    list_of_contents = ["".join(a), *splitted, "".join(b)]
    
    counts = 0
    for word in list_of_contents:
        result = 0
        for char in word:
            result += dictionary.index(char) + 1
        if result in dictionary_squences:
            counts += 1
    
    print(counts)
    
    
