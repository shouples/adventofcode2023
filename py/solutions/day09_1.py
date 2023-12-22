from solutions.utils import timer


def predict_next(readings: list[int]) -> int:
    diffs = []
    for i, reading in enumerate(readings):
        if i == len(readings) - 1:
            # at the last reading, can't subtract the next reading
            break
        # get the difference between the current reading and the next reading
        next_reading: int = readings[i + 1]
        diffs.append(next_reading - reading)

    # if all the diffs are the same, return the last reading + the diff
    if not len(set(diffs)) == 1:
        return readings[-1] + predict_next(diffs)

    return readings[-1] + diffs[0]


@timer
def solve(inputs: list[list[int]]) -> int:
    """High-level solution logic to call additional functions as needed."""
    next_readings = []
    for readings in inputs:
        next_reading: int = predict_next(readings)
        next_readings.append(next_reading)
    return sum(next_readings)


@timer
def load_input() -> list[list[int]]:
    """Read from an input file and handle any preprocessing."""
    inputs = open("../inputs/9.txt").readlines()

    readings = []
    for line in inputs:
        line_readings = [int(reading) for reading in line.split()]
        readings.append(line_readings)
    return readings


@timer
def run() -> None:
    inputs: list[list[int]] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
