import csv
import pprint
import collections



with open('players.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    players = collections.defaultdict(list)
    for line in reader:
        players[line['lastname']].append(
           {
                'name': line['name'],
                'lastname': line['lastname'],
                'age': line['age'],
                'points': line['points'],
            }
        )
# a. Top 3 graczy wg największej ilości zdobytych punktów
        a = collections.Counter(players['name'])
        print(a)
# b. Średnia wieku graczy
# c. Najczęściej występujące imię wśród graczy

# d. Średnia ilość punktów
# e. Maksymalna ilość punktów
# f. Minimalna ilość punktów
# g. Najstarszy gracz
