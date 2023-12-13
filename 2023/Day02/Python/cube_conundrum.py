from enum import Enum
import re


class BallColor(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

    def max_quantity(self) -> int:
        match self.value:
            case 0:
                return 12
            case 1:
                return 13
            case 2:
                return 14


class SingleExtraction():
    def __init__(self, string: str) -> None:
        self.quantity = int(re.findall('(\d+)', string)[0])
        string = string.replace(f"{self.quantity} ", '')
        self.color = BallColor[string.upper()]

    def is_valid(self) -> bool:
        return self.quantity <= self.color.max_quantity()
    
    def __repr__(self) -> str:
        return f"{self.quantity} {self.color.name}"


class Extraction():
    def __init__(self, string: str) -> None:
        self.extracions = [SingleExtraction(
            extraction_string.strip()) for extraction_string in string.split(',')]

    def is_valid(self) -> bool:
        return all([extracion.is_valid() for extracion in self.extracions])

    def get_red(self) -> int:
        return next((extraction.quantity for extraction in self.extracions if extraction.color == BallColor.RED), -1)

    def get_green(self) -> int:
        return next((extraction.quantity for extraction in self.extracions if extraction.color == BallColor.GREEN), -1)

    def get_blue(self) -> int:
        return next((extraction.quantity for extraction in self.extracions if extraction.color == BallColor.BLUE), -1)
    
    def __repr__(self) -> str:
        return f"{self.extracions}"


class Game():
    def __init__(self, string: str) -> None:
        self.index = int(re.findall('Game (\d+):', string)[0])
        string = string.replace(f'Game {self.index}: ', '')
        self.extractions = [Extraction(extractions_string.strip())
                            for extractions_string in string.split(';')]

    def is_valid(self) -> bool:
        return all([extraction.is_valid() for extraction in self.extractions])

    def get_power(self) -> int:
        min_red = max([extraction.get_red()
                      for extraction in self.extractions])
        min_green = max([extraction.get_green()
                        for extraction in self.extractions])
        min_blue = max([extraction.get_blue()
                       for extraction in self.extractions])
        return min_red * min_green * min_blue


class Games():
    def __init__(self, file_path: str) -> None:
        with open(file_path) as input_file:
            self.games = [Game(line) for line in input_file.readlines()]

    def get_valid_IDS(self):
        return sum([game.index for game in self.games if game.is_valid()])

    def get_sum_of_power(self):
        return sum([game.get_power() for game in self.games])


if __name__ == '__main__':
    # input: The relative path of input file
    # Ex: '2023\Day02\input.txt'
    file_path = input('Relative path of input file: ')
    g = Games(file_path)
    print(f"Sum of ID of valid Games: {g.get_valid_IDS()}")
    print(f"Sum of Power of Games: {g.get_sum_of_power()}")
