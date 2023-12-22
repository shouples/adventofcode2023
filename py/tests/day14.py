import pytest
from solutions import day14_1


def test_part1():
    input_str = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""
    assert day14_1.solve(input_str) == 136


@pytest.mark.skip(reason="admitted defeat 😢")
def test_part2():
    pass
