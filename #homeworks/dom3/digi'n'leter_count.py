user_input = input("Podaj dowolny ciąg znaków do obliczenia: ")

letters = 0
digits = 0

for i in user_input:
    if (i.isalpha()):
        letters += 1
    elif (i.isdecimal()):
        digits += 1
print(f"liczba cyfr w ciągu to {digits}, liczba liter w ciagu to {letters}.")
