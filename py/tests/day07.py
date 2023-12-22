from solutions import day07_1, day07_2


def test_part1():
    inputs = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
    assert day07_1.solve(inputs) == 6440


def test_part2():
    inputs = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
    assert day07_2.solve(inputs) == 5905
