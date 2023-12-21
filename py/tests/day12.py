import pytest
from solutions import day12_1


def test_part1():
    input_str = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()
    assert day12_1.solve(input_str) == 21


@pytest.mark.skip(reason="admitted defeat 😢")
def test_part2():
    pass
