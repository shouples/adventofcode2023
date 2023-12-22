from solutions import day06_1, day06_2


def test_part1():
    inputs = """Time:      7  15   30
Distance:  9  40  200""".splitlines()
    times = list(map(int, inputs[0].split()[1:]))
    distances = list(map(int, inputs[1].split()[1:]))
    assert day06_1.solve(times, distances) == 288


def test_part2():
    inputs = """Time:      7  15   30
Distance:  9  40  200""".splitlines()
    time = int(inputs[0].split(":")[1].replace(" ", ""))
    distance = int(inputs[1].split(":")[1].replace(" ", ""))
    assert day06_2.solve(time, distance) == 71503
