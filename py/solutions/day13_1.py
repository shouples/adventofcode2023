from typing import Optional

import pandas as pd
from IPython.display import Markdown
from solutions.utils import timer


def find_mirror_position(df: pd.DataFrame, v: bool = False, show=False) -> Optional[int]:
    max_score = 0
    for i in range(1, len(df) + 1):
        if i == len(df):
            # can't split on the last row
            continue

        top_rows = df.iloc[:i]
        bottom_rows = df.iloc[i:]

        if len(top_rows) > len(bottom_rows):
            # shorten top rows
            top_rows = top_rows.tail(len(bottom_rows))
        elif len(top_rows) < len(bottom_rows):
            # shorten bottom rows
            bottom_rows = bottom_rows.head(len(top_rows))

        # flip the bottom rows' index positions so they (potentially) match the top
        bottom_rows = bottom_rows.iloc[::-1]

        assert len(bottom_rows) == len(top_rows)

        # string comparisons on just the values is better than trying to compare the whole dataframe
        # portions, which will include the index values and columns by default
        t = top_rows.to_string(index=False, header=False)
        b = bottom_rows.to_string(index=False, header=False)
        if t == b:
            df_copy = df.copy()
            if v:
                # debug_df = debug_df.transpose()
                df_copy = df_copy.transpose()

            # last row's index + 1 in `top_rows` is the position of the mirror line
            last_index = top_rows.index[-1] + 1
            # 1x for mirroring against a vertical line, 100x for a horizontal line
            score = last_index * 100 if not v else last_index

            max_score += score
    return max_score


def find_mirror_lines(data: str, show: bool = False):
    rows = data.split("\n")
    df = pd.DataFrame([list(line) for line in rows]).astype(int)

    score = 0

    horizontal_line_score = find_mirror_position(df, show=show)
    if horizontal_line_score is not None:
        score += horizontal_line_score

    vertical_line_score = find_mirror_position(df.transpose(), v=True, show=show)
    if vertical_line_score is not None:
        score += vertical_line_score

    return score


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    total_score = 0
    for block in inputs:
        total_score += find_mirror_lines(block)
    return total_score


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/13.txt").read().strip().replace("#", "1").replace(".", "0").split("\n\n")


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
