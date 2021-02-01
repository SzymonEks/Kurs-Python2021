import re

# # Napisz program, który jako dane wejściowe przyjmuje hasło od użytkownika i sprawdza
# poprawność hasła względem poniższym kryteriów:
# a. Conajmniej jedna mała litera
# b. Conajmniej jedna cyfra
# c. Conajmniej jedna wielka litera
# d. Conajmniej jeden znak specjalny np. - @ #
# e. Minimalna długość hasła 8 znaków
# f. Maksymalna długość hasła 64 znaki (aby nikt nie wkleił całej treści Pana
# Tadeusza ;) )

print('Program sprawdza poprawność hasła względem poniższym kryteriów')
print('a. Conajmniej jedna mała litera')
print ('b. Conajmniej jedna cyfra')
print('c. Conajmniej jedna wielka litera')
print('d. Conajmniej jeden znak specjalny np. - @ #')
print('e. Minimalna długość hasła 8 znaków')
print('f. Maksymalna długość hasła 64 znaki')

password = input("Podaj hasło do sprawdzenia: ")
flag = 0
while True:
    if (len(password) < 8):
        flag = -1
        print("hasło za krótkie - Minimalna długość hasła 8 znaków")
    if (len(password) > 64):
        flag = -1
        print("hasło za długie - Maksymalna długość hasła 64 znaki")
    if not re.search("[a-z]", password):
        flag = -1
        print("Hasło nie zawiera coanjmiej jednej małej litery")
    if not re.search("[A-Z]", password):
        flag = -1
        print("Hasło nie zawiera coanjmiej jednej wielkiej litery")
    if not re.search("[0-9]", password):
        flag = -1
        print("Hasło nie zawiera coanjmiej jednej cyfry")
    if not re.search("[-@#]", password): #czy jest jakaś funkcja na znaki specjlane? coś jak ifalpha?
        flag = -1
        print("Hasło nie zawiera znaku specjlanego")
        break
    else:
        flag = 0
        print("Hasło poprawne")
        break

if flag == -1:
    print("Hasło nie poprawne")
