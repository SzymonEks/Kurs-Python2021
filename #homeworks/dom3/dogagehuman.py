human_age = float(input("Podaj wiek w latach ludzkich: "))

if human_age == 1:
    print("Wiek wiek w latach psich to 10.5")
elif human_age == 2:
    print("Wiek w latach psich to 21")
elif human_age >= 3:
    print('Wiek w latach psich to ' + str(((human_age - 2) * 4) + 21))
