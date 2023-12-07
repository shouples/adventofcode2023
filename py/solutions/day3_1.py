import string

from utils import timer

PART_SYMBOLS = {char for char in string.punctuation if char != "."}


def get_part_num_sum(rows) -> list[int]:
    part_nums = []
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
            # our checking_number against values above/below/left/right and diagonal for symbols
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
                char_left = row[left]
                char_right = row[right]
                chars_below = []
                if not bottom_row:
                    chars_below = rows[below][left : right + 1]

                if char_left in PART_SYMBOLS:
                    part_nums.append(int(checking_number))
                    continue
                if char_right in PART_SYMBOLS:
                    part_nums.append(int(checking_number))
                    continue
                if any([char in PART_SYMBOLS for char in chars_above]):
                    part_nums.append(int(checking_number))
                    continue
                if any([char in PART_SYMBOLS for char in chars_below]):
                    part_nums.append(int(checking_number))
                    continue

    return part_nums


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    nums = get_part_num_sum(inputs)
    return sum(nums)


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
