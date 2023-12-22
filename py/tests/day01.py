from solutions import day01_1, day01_2


def test_part1():
    inputs = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split()

    assert day01_1.solve(inputs) == 142


def test_part2():
    inputs = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split()

    assert day01_2.solve(inputs) == 281
