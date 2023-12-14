from itertools import combinations

from solutions.utils import timer


def find_possible_arrangements(spring_row: str, operational_counts: str) -> int:
    operational_group_counts = [int(c) for c in operational_counts.split(",")]

    num_operational_needed = sum(operational_group_counts) - spring_row.count("#")
    num_unknown = spring_row.count("?")

    possible_arrangements = 0
    # using the number of `#` needed, come up with combinations based on the number of `?`s
    for operational_positions in combinations(range(num_unknown), num_operational_needed):
        # cast as list so we can replace by index position
        spring_row_copy = list(spring_row)

        unknown_pos_index = 0
        for i in range(len(spring_row_copy)):
            if spring_row_copy[i] == "?":
                # replace with `#` if this combination has an operational position here
                if unknown_pos_index in operational_positions:
                    spring_row_copy[i] = "#"
                unknown_pos_index += 1

        # fill in any remaining gaps with `.`s
        new_string_row = "".join(spring_row_copy).replace("?", ".")

        # split into groups of `#` and check counts against operational_group_counts
        new_counts = [len(g) for g in new_string_row.split(".") if g]
        if new_counts == operational_group_counts:
            possible_arrangements += 1

    return possible_arrangements


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    arrangement_counts = 0
    for i, line in enumerate(inputs):
        spring_row, operational_counts = line.split()
        count = find_possible_arrangements(spring_row, operational_counts)
        arrangement_counts += count
    return arrangement_counts


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/12.txt").readlines()


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
