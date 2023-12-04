from utils import timer


class Card:
    id: int
    winning_numbers: list[int]
    numbers: list[int]

    def __init__(self, data: str):
        self.id, numbers = data.split(":")
        self.id = int(self.id.split()[-1])
        winning_numbers, guess_numbers = numbers.split("|")
        self.winning_numbers = [int(x) for x in winning_numbers.strip().split(" ") if x]
        self.numbers = [int(x) for x in guess_numbers.strip().split(" ") if x]

    @property
    def matching_numbers(self) -> list[int]:
        return [x for x in self.numbers if x in self.winning_numbers]

    @property
    def total_score(self) -> int:
        matches = self.matching_numbers
        if not matches:
            return 0
        score = 0
        for _ in matches:
            if not score:
                score = 1
            else:
                score *= 2
        return score


def get_score(inputs: list[str]) -> int:
    cards = [Card(x) for x in inputs]
    return sum([x.total_score for x in cards])


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    return get_score(inputs)


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/4.txt").read().splitlines()


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
