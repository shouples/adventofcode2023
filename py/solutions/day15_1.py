from solutions.utils import timer


def run_HASH(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


@timer
def solve(inputs: str) -> int:
    """High-level solution logic to call additional functions as needed."""
    values = [run_HASH(string) for string in inputs.split(",")]
    return sum(values)


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/15.txt").read()


@timer
def run() -> None:
    inputs: str = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
