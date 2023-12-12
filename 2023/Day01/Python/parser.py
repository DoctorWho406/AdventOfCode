class SimpleParser():
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

        self.file_path = file_path
        self.calibrations = list[int]()
        self.parse_file()

    def parse_file(self) -> None:
        with open(self.file_path) as input_file:
            for line in input_file.readlines():
                self.calibrations.append(self.parse_line(line))

    def parse_line(self, line: str) -> int:
        return (self.find_number(line, True) * 10) + self.find_number(line, False)

    def find_number(self, line: str, start: bool) -> int:
        for char in line if start else reversed(line):
            try:
                return int(char)
            except ValueError:
                pass

    def get_calibration_sum(self):
        return sum(self.calibrations)


if __name__ == '__main__':
    # input: The relative path of input file
    # Ex: '2023\Day01\input.txt'
    file_path = input('Relative path of input file: ')
    p = SimpleParser(file_path)
    print(
        f"Sum of calibrations (parsing only number): {p.get_calibration_sum()}")
