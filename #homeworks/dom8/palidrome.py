#
# with open('words.txt') as f:
#     lines = [line.strip() for line in f]

with open('words.txt') as f:
    lines = [line.strip() for line in f]
    palindromes = False
    for line in f:
        if isPalindrome(line.strip()):
            palindromes = True
            print(line.strip(), " is a palindrome.")

    return "palindromes found in {}".format(f) if palindroms else "no palindromes found."
