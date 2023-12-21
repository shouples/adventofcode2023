import pandas as pd
from solutions.utils import timer


def expand_universe(df: pd.DataFrame) -> pd.DataFrame:
    expanded_columns = []
    for i, col in enumerate(df.columns):
        # NOTE: we can't just `df.insert`, because if we have multiple columns missing galaxies,
        # we'll end up using an index value that's based on the original df, not the expanded one
        expanded_columns.append(df[col])
        if not df[col].sum():
            # no galaxies, add a new column to represent expansion
            expanded_columns.append(pd.Series(df[col], name=f"{col}e"))

    expanded_df = pd.concat(expanded_columns, axis=1)
    return expanded_df


def generate_universe(galaxy_data: str):
    universe_df = pd.DataFrame(
        [list(row) for row in galaxy_data.replace(".", "0").replace("#", "1").splitlines()]
    ).astype(int)

    # expand universal columns without galaxies
    universe_df = expand_universe(universe_df)
    # flip the universe to expand rows without galaxies
    universe_df = universe_df.transpose()
    universe_df = expand_universe(universe_df)
    # flip back
    universe_df = universe_df.transpose()

    return universe_df


def find_galaxies(universe_df: pd.DataFrame, expansion_scale: int) -> list[tuple[int, int]]:
    galaxies = []
    for i, col in enumerate(universe_df.columns):
        for j, row in enumerate(universe_df[col]):
            if row:
                # count how many rows/columns exist before this one that don't have galaxies
                galaxyless_columns = [
                    col for col in universe_df.columns[:i] if not universe_df[col].sum()
                ]
                num_galaxyless_columns = len(galaxyless_columns)
                galaxyless_rows = [
                    col
                    for col in universe_df.transpose().columns[:j]
                    if not universe_df.transpose()[col].sum()
                ]
                num_galaxyless_rows = len(galaxyless_rows)

                # adjust the position based on the expansion scale and number of galaxyless rows/columns
                adjusted_x = i + (num_galaxyless_columns * expansion_scale)
                adjust_y = j + (num_galaxyless_rows * expansion_scale)

                galaxies.append((adjusted_x, adjust_y))
    return galaxies


def get_shortest_distance_between_galaxies(
    universe_df: pd.DataFrame, galaxy_locations: list[tuple[int, int]]
) -> int:
    shortest_distances = {}
    for i, (x1, y1) in enumerate(galaxy_locations):
        for j, (x2, y2) in enumerate(galaxy_locations):
            if i == j:
                continue
            vertical_distance = abs(y1 - y2)
            horizontal_distance = abs(x1 - x2)
            total_distance = vertical_distance + horizontal_distance
            if (j, i) in shortest_distances:
                # we've already calculated this distance
                continue
            shortest_distances[(i, j)] = total_distance
    return shortest_distances


@timer
def solve(inputs: str, scale: int) -> int:
    """High-level solution logic to call additional functions as needed."""
    universe: pd.DataFrame = generate_universe(inputs)
    galaxies: list[tuple[int, int]] = find_galaxies(universe, scale)
    shortest_distances: int = get_shortest_distance_between_galaxies(universe, galaxies)
    return sum(shortest_distances.values())


@timer
def load_input() -> str:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/11.txt").read()


@timer
def run() -> None:
    inputs: str = load_input()
    solution = solve(inputs, 999_999)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
