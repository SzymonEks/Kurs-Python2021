import csv
from pprint import pprint
from collections import defaultdict

#def open_csv(filename='players.csv', delimiter=';'):
with open('players.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    players = defaultdict(list)
    print(reader.fieldnames)
    for line in reader:
        players[line['lastname']].append(
            {
                'name': line['name'],
                'lastname': line['lastname'],
                'age': line['age'],
                'points': line['points'],
            }
        )
pprint(players)
