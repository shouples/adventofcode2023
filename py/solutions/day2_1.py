from utils import timer


def build_games_data(inputs: list[str]) -> dict:
    games = {}
    for line in inputs:
        game_num, game_data = line.split(":")
        game_num = int(game_num.replace("Game ", ""))
        games[game_num] = {
            "red": [],
            "green": [],
            "blue": [],
        }
        game_rounds = game_data.strip().split(";")
        for game_round in game_rounds:
            pulls = game_round.split(", ")
            for pull in pulls:
                num, color = pull.split()
                games[game_num][color].append(int(num))
    return games


@timer
def solve(inputs: list[str]) -> int:
    games = build_games_data(inputs)
    possible_games = 0
    for game_num, color_info in games.items():
        # 12 red
        if any([color > 12 for color in color_info["red"]]):
            continue
        # 13 green
        if any([color > 13 for color in color_info["green"]]):
            continue
        # 14 blue
        if any([color > 14 for color in color_info["blue"]]):
            continue
        possible_games += game_num
    return possible_games


@timer
def load_input() -> list[str]:
    return open("../inputs/2.txt").readlines()


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
