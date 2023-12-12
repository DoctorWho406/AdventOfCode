import os
import re
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
            try:
                return int(char)
            except ValueError:
                pass

    def get_calibration_sum(self):
        return sum(self.calibrations)


class ComplexParser(SimpleParser):
    def __init__(self, file_path: str) -> None:
        self.literal_number = [
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
        regex = f"(\d|{'|'.join(self.literal_number)})" + (
            "" if start else f"(?!.*(\d|{'|'.join(self.literal_number)}))")
        match = re.search(regex, line)
        try:
            return int(match.group())
        except ValueError:
            return self.literal_number.index(match.group())


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
