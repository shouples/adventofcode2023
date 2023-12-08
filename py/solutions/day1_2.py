from solutions.utils import timer

digit_conversions = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_first_and_last_digits_with_conversion(line: str) -> int:
    first_digit = None
    last_digit = None

    line = line.strip()

    # iterate through the characters to get the first digit
    for i, c in enumerate(line):
        if first_digit is not None:
            break
        if c.isdigit():
            first_digit = c
            break
        for str_digit, digit in digit_conversions.items():
            if line[i:].startswith(str_digit):
                first_digit = str(digit)
                break

    # reverse the line and iterate through the characters to get the last digit
    for i, c in enumerate(line[::-1]):
        if last_digit is not None:
            break
        if c.isdigit():
            last_digit = c
            break
        # look for the spelled out digit in the not-reversed line, stepping back through the string
        # (there's probably a better way to do this)
        for str_digit, digit in digit_conversions.items():
            if i:
                if line[: -i + 1].endswith(str_digit):
                    last_digit = str(digit)
                    break
            else:
                if line.endswith(str_digit):
                    last_digit = str(digit)
                    break

    combined_value: str = f"{first_digit}{last_digit}"
    return int(combined_value)


@timer
def solve(inputs: list[str]) -> None:
    values: list[int] = [get_first_and_last_digits_with_conversion(line) for line in inputs]
    solution = sum(values)
    print(f"{solution=}")


@timer
def load_input() -> list[str]:
    return open("../inputs/1.txt").readlines()


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solve(inputs)


if __name__ == "__main__":
    run()
