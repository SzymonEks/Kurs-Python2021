floor = int(input("Podaj liczbe pięter: "))
for i in range(0, floor):
    for i in range(0, i + 1):
        print(end="#")
    print()