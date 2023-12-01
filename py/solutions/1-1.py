from utils import timer


def get_first_and_last_digits(line: str) -> int:
    first_digit = None
    last_digit = None

    line = line.strip()

    # iterate through the characters to get the first digit
    for c in line:
        if c.isdigit():
            first_digit = c
            break

    # reverse the line and iterate through the characters to get the last digit
    for c in line[::-1]:
        if c.isdigit():
            last_digit = c
            break

    combined_value: str = f"{first_digit}{last_digit}"
    return int(combined_value)


@timer
def solve(inputs) -> None:
    values: list[int] = [get_first_and_last_digits(line) for line in inputs]
    print(sum(values))


def run():
    # load input
    inputs = open("../inputs/1.txt").readlines()
    # process the solution
    solve(inputs)


if __name__ == "__main__":
    run()
