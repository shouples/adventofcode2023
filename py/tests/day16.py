from solutions import day16_1, day16_2


def test_part1():
    input_str = open("../inputs/16_test.txt").read()
    solution = day16_1.solve(input_str)
    assert solution == 46, solution


def test_part2():
    input_str = open("../inputs/16_test.txt").read()
    solution = day16_2.solve(input_str)
    assert solution == 51, solution
