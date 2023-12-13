from typing import Optional

from solutions.utils import timer


class MapPosition:
    can_connect_north = False
    can_connect_south = False
    can_connect_west = False
    can_connect_east = False

    def __init__(self, lat: int, lon: int):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other: "MapPosition") -> bool:
        if other is None:
            return False
        return self.coords == other.coords

    @property
    def coords(self) -> tuple[int, int]:
        return (self.lat, self.lon)

    def __repr__(self):
        return "░"


class WEPipe(MapPosition):
    can_connect_west = True
    can_connect_east = True

    def __repr__(self):
        return "═"


class NSPipe(MapPosition):
    can_connect_north = True
    can_connect_south = True

    def __repr__(self):
        return "║"


class NWPipe(MapPosition):
    can_connect_north = True
    can_connect_west = True

    def __repr__(self):
        return "╝"


class NEPipe(MapPosition):
    can_connect_north = True
    can_connect_east = True

    def __repr__(self):
        return "╚"


class SWPipe(MapPosition):
    can_connect_south = True
    can_connect_west = True

    def __repr__(self):
        return "╗"


class SEPipe(MapPosition):
    can_connect_south = True
    can_connect_east = True

    def __repr__(self):
        return "╔"


class StartPosition(MapPosition):
    can_connect_north = True
    can_connect_south = True
    can_connect_east = True
    can_connect_west = True

    def __repr__(self):
        return "O"


def convert_to_position(pos: str, lat: int, lon: int) -> MapPosition:
    if pos == ".":
        obj = MapPosition
    elif pos == "-":
        obj = WEPipe
    elif pos == "J":
        obj = NWPipe
    elif pos == "7":
        obj = SWPipe
    elif pos == "L":
        obj = NEPipe
    elif pos == "F":
        obj = SEPipe
    elif pos == "|":
        obj = NSPipe
    elif pos == "S":
        obj = StartPosition
    else:
        raise ValueError(f"Unknown position: {pos}")
    return obj(lat, lon)


class PipeMap:
    def __init__(self, map: str):
        self.data = self.generate_map(map)

    def generate_map(self, map: str) -> list[list[MapPosition]]:
        new_rows = []
        map_lines = map.splitlines()
        for lat, row in enumerate(map_lines):
            new_row = []
            for lon, pos in enumerate(row):
                obj = convert_to_position(pos, lat, lon)
                new_row.append(obj)
            new_rows.append(new_row)
        return new_rows


class MapPositionRunner:
    def __init__(self, map_str: str):
        self.pipe_map = PipeMap(map_str)

    @property
    def map_data(self) -> list[list[MapPosition]]:
        return self.pipe_map.data

    @property
    def starting_position(self) -> StartPosition:
        for row in self.map_data:
            for pos in row:
                if isinstance(pos, StartPosition):
                    return pos

    def __repr__(self) -> str:
        map_repr = ""
        for row in self.map_data:
            for pos in row:
                map_repr += repr(pos)
            map_repr += "\n"
        return map_repr

    def north_position(self, from_position: MapPosition) -> Optional[MapPosition]:
        if from_position.lat != 0 and from_position.can_connect_north:
            to_position: MapPosition = self.map_data[from_position.lat - 1][from_position.lon]
            if to_position.can_connect_south:
                return to_position
        return None

    def south_position(self, from_position: MapPosition) -> Optional[MapPosition]:
        if from_position.lat != len(self.map_data) - 1 and from_position.can_connect_south:
            to_position: MapPosition = self.map_data[from_position.lat + 1][from_position.lon]
            if to_position.can_connect_north:
                return to_position
        return None

    def west_position(self, from_position: MapPosition) -> Optional[MapPosition]:
        if from_position.lon != 0 and from_position.can_connect_west:
            to_position: MapPosition = self.map_data[from_position.lat][from_position.lon - 1]
            if to_position.can_connect_east:
                return to_position
        return None

    def east_position(self, from_position: MapPosition) -> Optional[MapPosition]:
        if (
            from_position.lon != len(self.map_data[from_position.lat]) - 1
            and from_position.can_connect_east
        ):
            to_position: MapPosition = self.map_data[from_position.lat][from_position.lon + 1]
            if to_position.can_connect_west:
                return to_position
        return None

    def available_moves(self, from_position: MapPosition):
        moves = []
        for direction in ("north", "south", "east", "west"):
            move = getattr(self, f"{direction}_position")(from_position)
            if move:
                moves.append(move)
        return moves

    def travel_loop(self) -> int:
        n_moves = 0
        last_position = None
        current_position = self.starting_position
        while True:
            moves = [
                m
                for m in self.available_moves(current_position)
                if m != last_position and m != self.starting_position
            ]
            if not moves:
                break

            last_position = current_position
            current_position = moves[0]
            n_moves += 1

        return (n_moves // 2) + 1


@timer
def solve(input_str: str) -> int:
    """High-level solution logic to call additional functions as needed."""
    runner = MapPositionRunner(input_str)
    return runner.travel_loop()


@timer
def load_input() -> str:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/10.txt").read()


@timer
def run() -> None:
    input_str: str = load_input()
    solution = solve(input_str)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
