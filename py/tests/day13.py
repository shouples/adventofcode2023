import pytest
from solutions import day13_1


def test_part1():
    input_str = (
        """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".strip()
        .replace("#", "1")
        .replace(".", "0")
        .split("\n\n")
    )
    assert day13_1.solve(input_str) == 405


@pytest.mark.skip(reason="admitted defeat 😢")
def test_part2():
    pass
