x = 1546
thousand_mod = x % 1000
hundred_mod = x % 100
ten_mod = x % 10

def extract_part(number):
    number = list(str(number))
    number.reverse()
    parts = []
    for i, e in enumerate(number):
        parts.append(int(e + ("0" * i)))
    return parts

def to_spell(number, idc):
    number = int(number)
    units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    dozens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    teens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    match idc:
        case "thousands":
            return units[number - 1] + "thousand"
        case "hundreds":
            return units[number - 1] + "hundred"
        case "teens":
            return teens[number - 2]
        case "dozens":
            return dozens[number - 1]
        case "units":
            return units[number - 1]
        case _:
            return ""

part = extract_part(x)
part.reverse()
print(part)

def convert(part):
    count = 0
    length = 0
    string = ""
    if len(part) >= 2:
        if part[-2] + part[-1] < 20 and part[-1] + part[-2] > 10:
            
            part = part[:-2] + [part[-2] + part[-1]]
            
        
    for u in part:
        if u >= 1000:
            spell = to_spell(u / 1000, "thousands")
            string += spell
            count += len(spell)
            length += 1
        elif u >= 100 and u < 1000:
            spell = to_spell(u / 100, "hundreds")
            string += spell
            count += len(spell)
            length += 1
        elif u < 100 and u > 19:
            spell = to_spell(u / 10, "teens")
            string += spell
            count += len(spell)
            length += 1
        elif u < 20 and u > 10:
            spell = to_spell(u % 10, "dozens")
            string += spell
            count += len(spell)
            length += 1
        elif u < 11 and u >= 1:
            spell = to_spell(u, "units")
            string += spell
            count += len(spell)
            length += 1
    if sum(part) > 99 and length > 1: 
        string+="and"
        count += len("and")
        #print(string)
    print(string)
    return count

counter = 0
for i in range(1, 1001):
    part = extract_part(i)
    part.reverse()
    counter += convert(part)
    if i == 546:
        print(convert(part))

print(counter)
    