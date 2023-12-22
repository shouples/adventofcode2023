from dataclasses import dataclass

import pandas as pd
from solutions.utils import timer


@dataclass
class PathState:
    heat_loss: int = 0
    position: tuple[int, int] = (0, 0)
    direction: str = "east"
    steps_since_turn: int = 0
    previous_state: "PathState" = None


class CruciblePusher:
    def __init__(self, df: pd.DataFrame):
        self.df = df

        self.start_position: tuple[int, int] = (0, 0)
        self.end_position: tuple[int, int] = (df.shape[0] - 1, df.shape[1] - 1)

        self.state_keys = set()

    def north_position(self, from_position: tuple[int, int]) -> tuple[int, int] | None:
        if from_position[0] == 0:
            # at the top row
            return None
        return from_position[0] - 1, from_position[1]

    def south_position(self, from_position: tuple[int, int]) -> tuple[int, int] | None:
        if from_position[0] == self.df.shape[0] - 1:
            # at the bottom row
            return None
        return from_position[0] + 1, from_position[1]

    def east_position(self, from_position: tuple[int, int]) -> tuple[int, int] | None:
        if from_position[1] == self.df.shape[1] - 1:
            # at the rightmost column
            return None
        return from_position[0], from_position[1] + 1

    def west_position(self, from_position: tuple[int, int]) -> tuple[int, int] | None:
        if from_position[1] == 0:
            # at the leftmost column
            return None
        return from_position[0], from_position[1] - 1

    def get_available_moves(self, from_state: PathState) -> dict[str, tuple[int, int]]:
        moves = {}
        directions = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
        }
        for direction, opposite_direction in directions.items():
            if from_state.direction == opposite_direction:
                # can't go backwards
                continue
            if from_state.direction == direction and from_state.steps_since_turn == 2:
                # can't go forward if we've already gone 3 steps
                continue
            dir_position = getattr(self, f"{direction}_position")
            if next_position := dir_position(from_state.position):
                moves[direction] = next_position
        return moves

    def calc_lowest_heat_loss(self, from_position: tuple[int, int], direction: str) -> int:
        start_state = PathState(
            heat_loss=0,
            position=from_position,
            direction=direction,
            steps_since_turn=0,
        )
        path_states = [start_state]

        while path_states:
            current_state = path_states.pop(0)
            if current_state.position == self.end_position:
                # hooray, we did it. return the heat loss and work backwards to get the path taken
                final_heat_loss = current_state.heat_loss

                path_taken = []
                while current_state is not None:
                    path_taken.append(current_state.position)
                    current_state: PathState = current_state.previous_state
                path_taken.reverse()

                return final_heat_loss, path_taken

            available_moves = self.get_available_moves(current_state)
            for to_direction, to_position in available_moves.items():
                heat_loss = current_state.heat_loss + self.df.iloc[to_position]

                steps_since_turn = current_state.steps_since_turn
                if to_direction == current_state.direction:
                    steps_since_turn += 1
                else:
                    # reset the steps since last turn
                    steps_since_turn = 0

                next_state = PathState(
                    heat_loss=heat_loss,
                    position=to_position,
                    direction=to_direction,
                    steps_since_turn=steps_since_turn,
                    previous_state=current_state,
                )
                # easier lookup than using a dataclass
                state_key = (
                    f"{next_state.position}{next_state.direction}{next_state.steps_since_turn}"
                )
                if state_key not in self.state_keys:
                    path_states.append(next_state)
                    self.state_keys.add(state_key)

                path_states = sorted(path_states, key=lambda s: s.heat_loss)

        # no path found
        return -1, []


def str_to_df(string: str) -> pd.DataFrame:
    return pd.DataFrame([[int(v) for v in row] for row in string.splitlines()])


@timer
def solve(input_str: str) -> int:
    """High-level solution logic to call additional functions as needed."""
    df = str_to_df(input_str)
    cp = CruciblePusher(df)
    heat_loss, path_taken = cp.calc_lowest_heat_loss(cp.start_position, "east")
    return heat_loss


@timer
def load_input() -> str:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/17.txt").read()


@timer
def run() -> None:
    input_str: str = load_input()
    solution = solve(input_str)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
