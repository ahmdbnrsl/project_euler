def check_palindrome(digit: int) -> bool:
    str_digit = str(digit)
    list_digit = list(str_digit)
    list_digit.reverse()
    new_digit = "".join(list_digit)
    return str_digit == new_digit

palindromes = []
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        digit = i * j
        is_palindrome = check_palindrome(digit)
        if is_palindrome: palindromes.append(digit)

largest_palindrome = max(palindromes)
print(largest_palindrome)