def decimal_to_bin(n):
    binaries = []
    while n >= 1:
        binaries = [str(n%2), *binaries]
        n = int(n/2)
    return "".join(binaries)

def is_palindrome(string):
    reverse = list(string)
    reverse.reverse()
    reverse = "".join(reverse)
    
    if string == reverse: return True
    return False

sums = 0
for i in range(1_000_001):
    if is_palindrome(str(i)):
        binary = decimal_to_bin(i)
        if is_palindrome(binary):
            print(i, binary)
            sums += i

print(sums)