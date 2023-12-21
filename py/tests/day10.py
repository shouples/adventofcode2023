import pytest
from solutions import day10_1


def test_part1():
    # example 1
    input_str = """.....
.S-7.
.|.|.
.L-J.
....."""
    assert day10_1.solve(input_str) == 4

    # example 2
    input_str2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
    assert day10_1.solve(input_str2) == 8


@pytest.mark.skip(reason="admitted defeat 😢")
def test_part2():
    pass
