from shapely import MultiPolygon, Polygon
from solutions.utils import timer


def create_dig_block(x, y) -> Polygon:
    # create a 1x1 block centered at x, y
    offset = 0.5
    return Polygon(
        [
            (x - offset, y - offset),
            (x + offset, y - offset),
            (x + offset, y + offset),
            (x - offset, y + offset),
        ]
    )


def dig_blocks(inputs: list[str]) -> Polygon:
    start_position = (0, 0)
    blocks = []
    for line in inputs:
        # create a block at the start position
        start_dig_block = create_dig_block(*start_position)

        # determine the new position
        # e.g. `U 7 (#4af7c3)`
        direction, distance, color = line.split()
        distance = int(distance)

        if direction == "R":
            new_position = (start_position[0] + distance, start_position[1])
        elif direction == "L":
            new_position = (start_position[0] - distance, start_position[1])
        elif direction == "U":
            new_position = (start_position[0], start_position[1] - distance)
        elif direction == "D":
            new_position = (start_position[0], start_position[1] + distance)

        # create a new block at the new position
        new_dig_block = create_dig_block(*new_position)

        # combine start_position and new_position into a rectangle
        multi_poly = MultiPolygon([start_dig_block, new_dig_block])
        bounding_box = multi_poly.bounds
        bbox_poly = Polygon(
            [
                (bounding_box[0], bounding_box[1]),
                (bounding_box[0], bounding_box[3]),
                (bounding_box[2], bounding_box[3]),
                (bounding_box[2], bounding_box[1]),
            ]
        )
        blocks.append(bbox_poly)
        # update start_position and move to the next line
        start_position = new_position

    # combine all blocks into one (multi)polygon
    all_blocks = blocks[0]
    for block in blocks[1:]:
        all_blocks = all_blocks.union(block)
    return all_blocks


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    dig_poly = dig_blocks(inputs)
    filled_dig_poly = Polygon(dig_poly.exterior)
    return int(filled_dig_poly.area)


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/18.txt").readlines()


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
