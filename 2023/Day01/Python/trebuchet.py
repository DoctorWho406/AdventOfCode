import os
import sys

global debug


class SimpleParser():
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.calibrations = list[int]()
        if debug:
            self.create_debug_file()
        self.parse_file()

    def create_debug_file(self):
        try:
            os.remove(self.get_debug_file_name())
        except FileNotFoundError:
            pass
        self.debug_file = open(self.get_debug_file_name(), 'x')

    def get_debug_file_name(self) -> str:
        return file_path.replace('input.txt', 'Python/output_simple.txt')

    def __del__(self):
        if debug:
            self.debug_file.close()

    def parse_file(self) -> None:
        print(f"Reading {self.file_path}")
        with open(self.file_path) as input_file:
            for line in input_file.readlines():
                self.calibrations.append(self.parse_line(line))

    def parse_line(self, line: str) -> int:
        decimal_value = self.find_number(line, True)
        unit_value = self.find_number(line, False)
        if debug:
            self.debug_file.write(
                f"{line}LEFT: {decimal_value}\t\tRIGHT: {unit_value}\n")
        return decimal_value * 10 + unit_value

    def find_number(self, line: str, start: bool) -> int:
        for char in line if start else reversed(line):
            if char.isdigit():
                return int(char)

    def get_calibration_sum(self):
        return sum(self.calibrations)


class ComplexParser(SimpleParser):
    def __init__(self, file_path: str) -> None:
        self.literal_numbers = [
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
        ]
        super().__init__(file_path)

    def get_debug_file_name(self) -> str:
        return file_path.replace('input.txt', 'Python/output_complex.txt')

    def find_number(self, line: str, start: bool) -> int:
        indexes = dict[int, int]()
        for number in range(len(self.literal_numbers)):
            string_index = line.find(self.literal_numbers[number]) if start else line.rfind(
                self.literal_numbers[number])
            number_index = line.find(
                str(number)) if start else line.rfind(str(number))
            if string_index != -1 or number_index != -1:
                if start:
                    if string_index == -1:
                        indexes[number] = number_index
                    elif number_index == -1:
                        indexes[number] = string_index
                    else:
                        indexes[number] = min(string_index, number_index)
                else:
                    indexes[number] = max(string_index, number_index)
        return min(indexes, key=indexes.get) if start else max(indexes, key=indexes.get)


if __name__ == '__main__':
    # input: The relative path of input file
    # Ex: '2023\Day01\input.txt'
    if (len(sys.argv) > 1 and sys.argv[1] == '--debug'):
        debug = True
    else:
        debug = False
    file_path = input('Relative path of input file: ')
    p = SimpleParser(file_path)
    print(
        f"Sum of calibrations (parsing only number): {p.get_calibration_sum()}")
    p = ComplexParser(file_path)
    print(
        f"Sum of calibrations (also parsing literal number): {p.get_calibration_sum()}")
