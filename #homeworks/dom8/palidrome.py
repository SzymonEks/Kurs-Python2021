filename = 'words.txt'

with open('words.txt') as f:
    lines = [line.strip() for line in f]
    for line in lines:
        if str(line)==(''):
           print('pusty wiersz')
        elif str(line) == str(line)[::-1]:
            print('is a palindrome')
        else:
            print('It`s not a palindrome')