import re


class Schema():
    def __init__(self, file_path: str) -> None:
        self.numbers = list[int]()
        validity_regex = '[^\d\.\s]'
        with open(file_path) as input_file:
            lines = input_file.readlines()
            row_numbers = len(lines)
            col_numbers = len(lines[0])
            for row in range(row_numbers):
                matches = re.finditer("(\d+)", lines[row])
                for match in matches:
                    print(f'{row}: DIGIT {match.group()} ', end='')
                    if row > 0:
                        matches = re.findall(
                            validity_regex, lines[row - 1][max(0, match.start() - 1):min(match.end() + 1, col_numbers)])
                        if matches:
                            self.numbers.append(int(match.group()))
                            print(f'VALID for TOP {matches}')
                            continue
                    matches = re.findall(validity_regex, lines[row][max(
                        0, match.start() - 1):min(match.end() + 1, col_numbers)])
                    if matches:
                        self.numbers.append(int(match.group()))
                        print(f'VALID {matches}')
                        continue
                    if row < row_numbers - 1:
                        matches = re.findall(
                            validity_regex, lines[row + 1][max(0, match.start() - 1):min(match.end() + 1, col_numbers)])
                        if matches:
                            self.numbers.append(int(match.group()))
                            print(f'VALID for BOTTOM {matches}')
                            continue
                    print(f'NOT VALID')

    def get_sum(self) -> int:
        return sum(self.numbers)


if __name__ == '__main__':
    # input: The relative path of input file
    # Ex: '2023\Day03\input.txt'
    file_path = input('Relative path of input file: ')
    s = Schema(file_path)
    print(s.get_sum())
