def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


text = input("podaj słowo do zaszyfrowania ")
s = 4
print("Tekst : " + text)
print("przesunięcie : " + str(s))
print("Szyfr: " + encrypt(text, s))
