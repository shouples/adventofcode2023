from solutions.utils import timer


def run_HASH(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def get_box_values(string: str) -> int:
    boxes = {}
    for label_str in string.split(","):
        # rn=1, cm-, qp=3, etc
        if "=" in label_str:
            # add/replace a label to a box
            label, focal_strength = label_str.split("=")
            box_num = run_HASH(label)
            if box_num not in boxes:
                boxes[box_num] = {}
            boxes[box_num][label] = focal_strength
        else:
            # remove a label from a box
            label = label_str.strip("-")
            box_num = run_HASH(label)
            boxes.get(box_num, {}).pop(label, None)

    values = []
    for box_num, label_data in boxes.items():
        # calculate the focusing power of each box's contents
        for i, (label, focal_strength) in enumerate(label_data.items()):
            value = (int(box_num) + 1) * (i + 1) * int(focal_strength)
            values.append(value)

    return sum(values)


@timer
def solve(inputs: str) -> int:
    """High-level solution logic to call additional functions as needed."""
    return get_box_values(inputs)


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/15.txt").read()


@timer
def run() -> None:
    inputs: str = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
