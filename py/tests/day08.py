import pytest
from solutions import day08_1


def test_part1():
    # example 1
    input_str = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
    directions, branch_data = input_str.split("\n\n")
    branch_lines = branch_data.split("\n")
    branches = day08_1.create_branches(branch_lines)
    assert day08_1.solve(directions, branches) == 2

    # example 2
    input_str2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
    directions2, branch_data2 = input_str2.split("\n\n")
    branch_lines2 = branch_data2.split("\n")
    branches2 = day08_1.create_branches(branch_lines2)
    assert day08_1.solve(directions2, branches2) == 6


@pytest.mark.skip(reason="admitted defeat 😢")
def test_part2():
    pass
