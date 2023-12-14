import re


class Schema():
    def __init__(self, file_path: str) -> None:
        self.numbers = list[int]()
        with open(file_path) as input_file:
            lines = input_file.readlines()
            row_numbers = len(lines)
            col_numbers = len(lines[0])
            for row in range(row_numbers):
                matches = re.finditer("(\d+)", lines[row])
                for match in matches:
                    if row > 0 and re.findall('[^\d\.]', lines[row - 1][max(0, match.start() - 1):min(match.end() + 2, col_numbers)]):
                        self.numbers.append(int(match.group()))
                        continue
                    if re.findall('[^\d\.]', lines[row][max(0, match.start() - 1):min(match.end() + 2, col_numbers)]):
                        self.numbers.append(int(match.group()))
                        continue
                    if row < row_numbers - 1 and re.findall('[^\d\.]', lines[row + 1][max(0, match.start() - 1):min(match.end() + 2, col_numbers)]):
                        self.numbers.append(int(match.group()))
                        continue
                    print(f'{row}: DIGIT {match.group()} NOT VALID')

    def get_sum(self) -> int:
        return sum(self.numbers)


if __name__ == '__main__':
    # input: The relative path of input file
    # Ex: '2023\Day03\input.txt'
    # file_path = input('Relative path of input file: ')
    file_path = '2023\Day03\input.txt'
    s = Schema(file_path)
    # 420712    LOW
    # 395780    LOW
    # 531491    HIGH
    # 538346
    # 531491
    print(s.get_sum())
