from solutions.utils import timer


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


def get_scratchcard_counts(inputs: list[str]) -> list[int]:
    cards = [Card(x) for x in inputs]

    card_counts = {}
    for card in cards:
        if card.id not in card_counts:
            card_counts[card.id] = 1
        num_matching_numbers = len(card.matching_numbers)
        card_copies_to_make = [card.id + i for i in range(1, num_matching_numbers + 1)]
        for following_card_id in card_copies_to_make:
            if following_card_id not in card_counts:
                card_counts[following_card_id] = 1
            # increase the count of following cards
            card_counts[following_card_id] += card_counts[card.id]

    return sum(card_counts.values())


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    return get_scratchcard_counts(inputs)


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
