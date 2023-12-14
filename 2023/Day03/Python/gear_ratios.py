import re


class Vector():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vector):
            return self.x == __value.x and self.y == __value.y
        return False

    def __hash__(self) -> int:
        return self.x.__hash__() ^ self.y.__hash__()

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


class Schema():
    def __init__(self, file_path: str) -> None:
        self.numbers = list[int]()
        self.gears = dict[Vector, list[int]]()
        validity_regex = '([^\d\.\s])'
        with open(file_path) as input_file:
            lines = input_file.readlines()
            row_numbers = len(lines)
            col_numbers = len(lines[0])
            for row in range(row_numbers):
                matches = re.finditer("(\d+)", lines[row])
                for match in matches:
                    is_valid = False
                    if row > 0:
                        nearest_matches = list(re.finditer(
                            validity_regex, lines[row - 1][max(0, match.start() - 1):min(match.end() + 1, col_numbers)]))
                        if nearest_matches:
                            is_valid = True
                            for gear in [nearest_match for nearest_match in nearest_matches if '*' in nearest_match.group()]:
                                self.gears.setdefault(
                                    Vector(max(0, match.start() - 1) + gear.start(), row-1), []).append(int(match.group()))
                    nearest_matches = list(re.finditer(validity_regex, lines[row][max(
                        0, match.start() - 1):min(match.end() + 1, col_numbers)]))
                    if nearest_matches:
                        is_valid = True
                        for gear in [nearest_match for nearest_match in nearest_matches if '*' in nearest_match.group()]:
                            self.gears.setdefault(
                                Vector(max(0, match.start() - 1) + gear.start(), row), []).append(int(match.group()))
                    if row < row_numbers - 1:
                        nearest_matches = list(re.finditer(
                            validity_regex, lines[row + 1][max(0, match.start() - 1):min(match.end() + 1, col_numbers)]))
                        if nearest_matches:
                            is_valid = True
                            for gear in [nearest_match for nearest_match in nearest_matches if '*' in nearest_match.group()]:
                                self.gears.setdefault(
                                    Vector(max(0, match.start() - 1) + gear.start(), row+1), []).append(int(match.group()))
                    if is_valid:
                        is_valid = False
                        self.numbers.append(int(match.group()))

    def get_sum(self) -> int:
        return sum(self.numbers)

    def get_gears(self) -> int:
        return sum([gear[0] * gear[1] for gear in self.gears.values() if len(gear) == 2])


if __name__ == '__main__':
    # input: The relative path of input file
    # Ex: '2023\Day03\input.txt'
    # file_path = input('Relative path of input file: ')
    file_path = '2023\Day03\input.txt'
    s = Schema(file_path)
    print(f'Sum of all parts: {s.get_sum()}')
    print(f'Sum of all gear ratios: {s.get_gears()}')
