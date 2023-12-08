from solutions.utils import timer


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


def get_game_powers(game: dict) -> int:
    red = max(game["red"])
    green = max(game["green"])
    blue = max(game["blue"])
    return red * green * blue


@timer
def solve(inputs: list[str]) -> int:
    games = build_games_data(inputs)
    power_sum = 0
    for _, game in games.items():
        power_sum += get_game_powers(game)
    return power_sum


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
