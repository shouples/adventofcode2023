from solutions import day09_1, day09_2


def test_part1():
    inputs = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

    readings = []
    for line in inputs:
        line_readings = [int(reading) for reading in line.split()]
        readings.append(line_readings)

    assert day09_1.solve(readings) == 114


def test_part2():
    inputs = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

    readings = []
    for line in inputs:
        line_readings = [int(reading) for reading in line.split()]
        readings.append(line_readings)

    assert day09_2.solve(readings) == 2
