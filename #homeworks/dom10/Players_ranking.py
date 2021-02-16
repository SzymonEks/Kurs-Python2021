# Wykorzystując paradygmant programowania obiektowego zamodeluj klasę(y) potrzebne do utworzenia rankingu graczy, korzystając z danych w pliku players.csv.
# Podpowiedź: przestudiuj kod z zajęć nr 10, rozwiązanie jest bardzo podobne.
# Wyświetlenie TOP 10 graczy.
# Wyświetlenie średniej ilości zdobytych punktów.
# Możliwość sortowania wyników rosnąco i malejąco.
import csv

class Player:
    def __init__(self, ID, name, score, age):
        self.ID = ID
        self.name = name
        self.score = score
        self.age = age

    def __str__(self):
        return f'{self.ID} {self.name} {self.score} {self.age}'

class PlayersRanking:

    def __init__(self):
        self.ranking = []

    def add_player(self, player):
        self.ranking.append(player)

    def from_csv(self, filename, delimiter=','):
        with open(filename, 'r') as players_file:
            reader = csv.DictReader(players_file, delimiter=delimiter)
            for player_data in reader:
                player = Player(
                    player_data['ID'],
                    player_data['name'],
                    player_data['score'],
                    player_data['age'],
                )
                self.add_player(player)

    def display_all(self):
        for player in self.ranking:
            print(player)

    def sort(self, reverse=False):
        self.ranking.sort(key=lambda player: player.score, reverse=True)



if __name__ == '__main__':

    Ranking = PlayersRanking()
    Ranking.from_csv('players.csv')
    Ranking.sort()
    Ranking.display_all()



