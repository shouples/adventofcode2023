from collections import Counter

from solutions.utils import timer

CARD_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Card:
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other: "Card") -> bool:
        return self.value == other.value

    def __gt__(self, other: "Card") -> bool:
        return self.score > other.score

    def __lt__(self, other: "Card") -> bool:
        return self.score < self.score

    def __repr__(self) -> str:
        return f"<Card {self.value!r}>"

    @property
    def score(self) -> int:
        return CARD_RANKS.index(self.value)


HAND_RANKS = ["HC", "1P", "2P", "3K", "FH", "4K", "5K"]


class CardHand:
    def __init__(self, hand_data: str):
        self.raw_cards, bid = hand_data.split()
        self.bid = int(bid)
        self.cards: list[Card] = [Card(value) for value in self.raw_cards]

        self.card_counts: dict[str, int] = Counter(card.value for card in self.cards)

        self.one_pair = [count for count in self.card_counts.values() if count == 2]
        self.two_pair = len(self.one_pair) == 2
        self.three_of_a_kind = [count for count in self.card_counts.values() if count == 3]
        self.full_house = self.one_pair and self.three_of_a_kind
        self.four_of_a_kind = [count for count in self.card_counts.values() if count == 4]
        self.five_of_a_kind = [count for count in self.card_counts.values() if count == 5]

    @property
    def rank(self) -> str:
        if self.five_of_a_kind:
            return "5K"
        elif self.four_of_a_kind:
            return "4K"
        elif self.full_house:
            return "FH"
        elif self.three_of_a_kind:
            return "3K"
        elif self.two_pair:
            return "2P"
        elif self.one_pair:
            return "1P"
        else:
            return "HC"

    @property
    def rank_score(self) -> int:
        hand_score = HAND_RANKS.index(self.rank) * 1_000_000_000
        hand_score += self.cards[0].score * 10_000_000
        hand_score += self.cards[1].score * 100_000
        hand_score += self.cards[2].score * 1_000
        hand_score += self.cards[3].score * 10
        hand_score += self.cards[4].score
        return hand_score

    def __repr__(self) -> str:
        return f"<CardHand {self.raw_cards}: {self.rank} (score={self.rank_score})>"

    def __eq__(self, other: "CardHand") -> bool:
        return self.cards == other.cards

    def __gt__(self, other: "CardHand") -> bool:
        for card, other_card in zip(self.cards, other.cards):
            if card == other_card:
                continue
            return card > other_card

    def __lt__(self, other: "CardHand") -> bool:
        for card, other_card in zip(self.cards, other.cards):
            if card == other_card:
                continue
            return card < other_card


def calculate_winnings(hands) -> int:
    winnings = 0
    for rank, hand in enumerate(hands):
        rank_multiplier = rank + 1
        hand_winning = hand.bid * rank_multiplier
        winnings += hand_winning
    return winnings


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    hands = sorted([CardHand(hand_data) for hand_data in inputs], key=lambda x: x.rank_score)
    return calculate_winnings(hands)


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/7.txt").read().splitlines()


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
