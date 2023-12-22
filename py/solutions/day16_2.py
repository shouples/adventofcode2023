from concurrent.futures import ProcessPoolExecutor, as_completed

from solutions.utils import timer


class BeamMap:
    def __init__(self, input_string: str):
        self.grid = self.generate_map(input_string)
        self.steps_taken: list[tuple[tuple[int, int], str]] = []

    def generate_map(self, input_string: str) -> list[list[str]]:
        return [list(line) for line in input_string.splitlines()]

    def grid_value(self, position: tuple[int, int]) -> str:
        y, x = position
        return self.grid[y][x]

    @property
    def beam_positions(self) -> set[tuple[int, int]]:
        return set([position for position, _ in self.steps_taken])

    def left_position(self, position: tuple[int, int]) -> tuple[int, int] | None:
        if self.at_left_column(position):
            return None
        y, x = position
        return (y, x - 1)

    def right_position(self, position: tuple[int, int]) -> tuple[int, int] | None:
        if self.at_right_column(position):
            return None
        y, x = position
        return (y, x + 1)

    def up_position(self, position: tuple[int, int]) -> tuple[int, int] | None:
        if self.at_top_row(position):
            return None
        y, x = position
        return (y - 1, x)

    def down_position(self, position: tuple[int, int]) -> tuple[int, int] | None:
        if self.at_bottom_row(position):
            return None
        y, x = position
        return (y + 1, x)

    def at_top_row(self, position: tuple[int, int]) -> bool:
        return position[0] == 0

    def at_bottom_row(self, position: tuple[int, int]) -> bool:
        return position[0] == len(self.grid) - 1

    def at_left_column(self, position: tuple[int, int]) -> bool:
        return position[1] == 0

    def at_right_column(self, position: tuple[int, int]) -> bool:
        return position[1] == len(self.grid[position[0]]) - 1

    def available_moves(
        self,
        from_position: tuple[int, int],
        direction: str,
    ) -> list[tuple[tuple[int, int], str]]:
        position_value = self.grid_value(from_position)

        moves = []
        if position_value == "|":
            if direction in ["L", "R"]:
                # split into two vertical moves
                if up := self.up_position(from_position):
                    moves.append((up, "U"))
                if down := self.down_position(from_position):
                    moves.append((down, "D"))
            elif direction == "U":
                # pass through
                if up := self.up_position(from_position):
                    moves.append((up, "U"))
            elif direction == "D":
                # pass through
                if down := self.down_position(from_position):
                    moves.append((down, "D"))

        elif position_value == "-":
            if direction in ["U", "D"]:
                # split into two horizontal moves
                if left := self.left_position(from_position):
                    moves.append((left, "L"))
                if right := self.right_position(from_position):
                    moves.append((right, "R"))
            elif direction == "L":
                # pass through
                if left := self.left_position(from_position):
                    moves.append((left, "L"))
            elif direction == "R":
                # pass through
                if right := self.right_position(from_position):
                    moves.append((right, "R"))

        elif position_value == "/":
            if direction == "U":
                if right := self.right_position(from_position):
                    moves.append((right, "R"))
            elif direction == "R":
                if up := self.up_position(from_position):
                    moves.append((up, "U"))
            elif direction == "D":
                if left := self.left_position(from_position):
                    moves.append((left, "L"))
            elif direction == "L":
                if down := self.down_position(from_position):
                    moves.append((down, "D"))

        elif position_value == "\\":
            if direction == "U":
                if left := self.left_position(from_position):
                    moves.append((left, "L"))
            elif direction == "L":
                if up := self.up_position(from_position):
                    moves.append((up, "U"))
            elif direction == "D":
                if right := self.right_position(from_position):
                    moves.append((right, "R"))
            elif direction == "R":
                if down := self.down_position(from_position):
                    moves.append((down, "D"))

        else:
            # regular ground, no adjustments
            if direction == "U":
                if up := self.up_position(from_position):
                    moves.append((up, direction))
            elif direction == "L":
                if left := self.left_position(from_position):
                    moves.append((left, direction))
            elif direction == "D":
                if down := self.down_position(from_position):
                    moves.append((down, direction))
            elif direction == "R":
                if right := self.right_position(from_position):
                    moves.append((right, direction))

        return moves

    def move(self, from_position: tuple[int, int], direction: str) -> int:
        self.steps_taken.append((from_position, direction))

        available_moves = self.available_moves(from_position, direction)
        while available_moves:
            next_moves = []
            for to_position, new_direction in available_moves:
                if to_position is None:
                    continue
                if (to_position, new_direction) in self.steps_taken:
                    continue
                self.steps_taken.append((to_position, new_direction))
                next_moves += self.available_moves(to_position, new_direction)
            available_moves = next_moves

        return len(self.beam_positions)


@timer
def solve(input_str: str) -> int:
    """High-level solution logic to call additional functions as needed."""
    ex = ProcessPoolExecutor()
    tasks = []

    beam_map = BeamMap(input_str)
    most_tiles_energized = 0
    for direction in ["R", "D", "L", "U"]:
        if direction in ["L", "R"]:
            col = 0 if direction == "R" else len(beam_map.grid[0]) - 1
            for row in range(len(beam_map.grid)):
                # reset progress
                beam_map.steps_taken = []
                task = ex.submit(
                    beam_map.move,
                    from_position=(row, col),
                    direction=direction,
                )
                tasks.append(task)
        else:
            # "U"/"D"
            row = 0 if direction == "D" else len(beam_map.grid) - 1
            for col in range(len(beam_map.grid[0])):
                # reset progress
                beam_map.steps_taken = []
                task = ex.submit(
                    beam_map.move,
                    from_position=(row, col),
                    direction=direction,
                )
                tasks.append(task)

    for task in as_completed(tasks):
        tiles_energized = task.result()
        if tiles_energized > most_tiles_energized:
            most_tiles_energized = tiles_energized

    ex.shutdown()

    return most_tiles_energized


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/16.txt").read()


@timer
def run() -> None:
    input_str: str = load_input()
    solution = solve(input_str)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
