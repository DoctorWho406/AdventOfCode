import re


class Card():
    def __init__(self, string: str) -> None:
        card, string = string.split(':')
        self.id = int(re.findall('(\d+)', card)[0])
        winning_numbers, numbers = string.split('|')
        self.winning_numbers = [int(number.strip())
                                for number in re.findall('\d+', winning_numbers)]
        self.numbers = [int(number.strip())
                        for number in re.findall('\d+', numbers)]

    def get_my_winning_numbers(self) -> list[int]:
        return [number for number in self.numbers if number in self.winning_numbers]

    def get_score(self) -> int:
        winning_number = len(self.get_my_winning_numbers())
        return 2 ** (winning_number - 1) if winning_number > 0 else 0


class Game():
    def __init__(self, file_path: str) -> None:
        with open(file_path) as input_file:
            self.games = [Card(line) for line in input_file.readlines()]

    def get_score(self) -> int:
        return sum(game.get_score() for game in self.games)


if __name__ == '__main__':
    # input: The relative path of input file
    # Ex: '2023\Day04\input.txt'
    file_path = input('Relative path of input file: ')
    g = Game(file_path)
    print(g.get_score())
