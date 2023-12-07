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
def solve(time: int, distance: int) -> int:
    """High-level solution logic to call additional functions as needed."""
    return calc_possible_acceleration(time, distance)


@timer
def load_input() -> tuple[int, int]:
    """Read from an input file and handle any preprocessing."""
    inputs = open("../inputs/6.txt").read().split("\n")
    # Time:      7  15   30
    # Distance:  9  40  200
    time = int(inputs[0].split(":")[1].replace(" ", ""))
    distance = int(inputs[1].split(":")[1].replace(" ", ""))
    return time, distance


@timer
def run() -> None:
    time, distance = load_input()
    solution = solve(time, distance)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
