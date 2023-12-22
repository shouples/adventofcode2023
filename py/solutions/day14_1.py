import pandas as pd
from solutions.utils import timer


def move_rocks(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df.copy()

    for col in new_df.columns:
        column_values = new_df[col].values

        # find groups between rock_positions
        rock_groups = str("".join([str(x) for x in column_values])).split("1")
        # sort each group in reverse order so the circle rocks are at the top
        new_value_groups = []
        for group in rock_groups:
            new_values = "".join(sorted(group, reverse=True))
            new_value_groups.append(new_values)
        # join them back together with the cube rocks
        new_column_values = "1".join(new_value_groups)

        new_row_data = [int(row) for row in new_column_values]
        new_df[col] = new_row_data

    return new_df


def calculate_beam_load(df) -> int:
    # reversed 1-indexed list of the number
    new_index = list(reversed(range(1, len(df) + 1)))

    weight = 0
    for i, scale in enumerate(new_index):
        # 10, 9, 8...etc
        row_weight = len([v for v in df.iloc[i].values if v == 2])
        weight += row_weight * scale
    return weight


def str_to_df(input_str: str) -> pd.DataFrame:
    df = pd.DataFrame([list(row) for row in input_str.splitlines()])
    # convert `O` to 2, `#` to 1 and `.` to 0
    df = df.replace({"O": 2, "#": 1, ".": 0})
    return df


@timer
def solve(input_str: str) -> int:
    """High-level solution logic to call additional functions as needed."""
    df = str_to_df(input_str)
    df = move_rocks(df)
    return calculate_beam_load(df)


@timer
def load_input() -> str:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/14.txt").read()


@timer
def run() -> None:
    input_str: str = load_input()
    solution = solve(input_str)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
