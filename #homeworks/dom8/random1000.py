# Wygeneruj dwie listy po 1000 elementów, w której będą się znajdować liczby losowe z
# przedziału 1-1000(randint). Porównaj obydwie listy i wyświetl:
# a. Liczby znajdujące się w obydwu listach.
# b. Liczby znajdujące się tylko w pierwszej liście.
# c. Liczby znajdujące się tylko w drugiej liście.
# d. Liczbę wystąpień każdej z liczby w obydwu listach i wyświetl top 3 najczęściej występujące w każdej z nich.
# e. Obydwie listy posortowane rosnąco i malejąco.


import random
import collections

random_list_1 = []
for i in range(0,100):
    n = random.randint(0,1000)
    random_list_1.append(n)

random_list_2 = []
for i in range(0,100):
    n = random.randint(0,1000)
    random_list_2.append(n)

a = set(random_list_1)
b = set(random_list_2)
print(f'Liczby znajdujące się w obydwu listach: ', a & b)
print(f'Liczby znajdujące się tylko w pierwszej liście: ', a - b)
print(f'Liczby znajdujące się tylko w drugiej liście:  ', b - a)
print(f'top 3 najczęściej występujące w każdej liście:  ', collections.Counter(random_list_2 + random_list_1).most_common(3))
sorted_up_random_list_1 = sorted(random_list_1, key=None, reverse=False)
print(f'Lista_1 rosnąco :', sorted_up_random_list_1)
sorted_down_random_list_1 = sorted(random_list_1, key=None, reverse=True)
print(f'Lista_1 malejąco :', sorted_down_random_list_1)
sorted_up_random_list_2 = sorted(random_list_1, key=None, reverse=False)
print(f'Lista_2 rosnąco :', sorted_up_random_list_2)
sorted_down_random_list_2 = sorted(random_list_2, key=None, reverse=True)
print(f'Lista_2 malejąco :', sorted_down_random_list_2)
