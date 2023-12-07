from collections import defaultdict

from utils import timer

GEAR_SYMBOL = "*"


def get_gear_power(rows) -> dict:
    gear_powers = defaultdict(list)
    for i, row in enumerate(rows):
        last_position = len(row) - 1

        # flags to determine whether we can check above/below the current row
        top_row = i == 0
        bottom_row = i == last_position

        # build up a string as we find numbers in the row
        checking_number = ""
        for char_index, char in enumerate(row):
            if not char.isdigit():
                checking_number = ""
                continue

            checking_number += char
            # if we're at the end of the row, or the next char isn't a digit, it's time to check
            # our checking_number against values above/below/left/right and diagonal for gears
            if char_index == last_position or not row[char_index + 1].isdigit():
                above = i - 1
                below = i + 1
                left = max(0, char_index - len(checking_number))
                right = min(char_index + 1, len(row) - 1)

                # check all around the current number, e.g.:
                # xxxxx
                # y123y
                # zzzzz

                chars_above = []
                if not top_row:
                    chars_above = rows[above][left : right + 1]

                chars_below = []
                if not bottom_row:
                    chars_below = rows[below][left : right + 1]

                char_left = row[left]
                if char_left == GEAR_SYMBOL:
                    gear_powers[(i, left)].append(int(checking_number))

                char_right = row[right]
                if char_right == GEAR_SYMBOL:
                    gear_powers[(i, right)].append(int(checking_number))

                if GEAR_SYMBOL in chars_above:
                    gear_index = left + chars_above.index(GEAR_SYMBOL)
                    gear_powers[(above, gear_index)].append(int(checking_number))

                if GEAR_SYMBOL in chars_below:
                    gear_index = left + chars_below.index(GEAR_SYMBOL)
                    gear_powers[(below, gear_index)].append(int(checking_number))

    return gear_powers


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    powers = get_gear_power(inputs)
    total_power = 0
    for part_numbers in powers.values():
        if len(part_numbers) > 1:
            power = 1
            for part_number in part_numbers:
                power *= part_number
            total_power += power
    return total_power


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    rows = open("../inputs/3.txt").readlines()
    return [row.strip() for row in rows]


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
