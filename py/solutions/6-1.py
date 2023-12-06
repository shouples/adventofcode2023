from utils import timer


def calc_possible_acceleration(race_time: int, race_dist: int) -> int:
    possible_accelerations = 0
    for button_press_duration in range(race_time):
        if button_press_duration == 0 or button_press_duration == race_time:
            # button wasn't pressed or was never released, so acceleration was 0 and distance was 0
            continue

        # button was pressed for button_press_duration seconds
        travel_duration = race_time - button_press_duration
        # button_press_duration=3 would mean we're traveling for 3mm per ms, so for the rest of the
        # time we're traveling at speed=button_press_duration mm/ms
        distance_covered = travel_duration * button_press_duration
        if distance_covered > race_dist:
            # we beat the record, hooray
            possible_accelerations += 1
    return possible_accelerations


@timer
def solve(times: list[int], distances: list[int]) -> int:
    """High-level solution logic to call additional functions as needed."""
    score = 1
    for time, dist in zip(times, distances):
        score *= calc_possible_acceleration(time, dist)
    return score


@timer
def load_input() -> tuple[list[int], list[int]]:
    """Read from an input file and handle any preprocessing."""
    inputs = open("../inputs/6.txt").read().split("\n")
    # Time:      7  15   30
    # Distance:  9  40  200
    times = list(map(int, inputs[0].split()[1:]))
    distances = list(map(int, inputs[1].split()[1:]))
    return times, distances


@timer
def run() -> None:
    times, distances = load_input()
    solution = solve(times, distances)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
