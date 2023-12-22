from solutions.utils import timer


class NodeBranch:
    def __init__(self, branches: dict, directions: str, moves: int = 0):
        self.branches = branches
        self.directions = directions
        self.moves = moves

    def traverse(self, starting_node: list[str]) -> int:
        current_node = starting_node

        for direction in self.directions:
            self.moves += 1

            if direction == "L":
                next_node = self.branches[current_node][0]
            elif direction == "R":
                next_node = self.branches[current_node][1]

            current_node = next_node
            if current_node == "ZZZ":
                # hooray, we did it
                break

        if current_node != "ZZZ":
            # time to do it all over again
            return self.traverse(current_node)

        return self.moves


def create_branches(branch_data: list[str]) -> dict:
    branches = {}
    for branch in branch_data:
        node_name, left_right = branch.split(" = ")
        left, right = left_right.strip("()").split(", ")
        # "AAA = (BBB, CCC)"
        branches[node_name] = (left, right)
    return branches


@timer
def solve(directions: str, branches: dict[str, tuple[str, str]]) -> int:
    """High-level solution logic to call additional functions as needed."""
    nb = NodeBranch(branches, directions)
    moves = nb.traverse(starting_node="AAA")
    return moves


@timer
def load_input() -> tuple[str, dict[str, tuple[str, str]]]:
    """Read from an input file and handle any preprocessing."""
    input_str = open("../inputs/8.txt").read()
    directions, branch_data = input_str.split("\n\n")
    branch_lines = branch_data.split("\n")
    branches = create_branches(branch_lines)
    return directions, branches


@timer
def run() -> None:
    directions, branches = load_input()
    solution = solve(directions, branches)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
