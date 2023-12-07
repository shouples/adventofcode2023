use adventofcode2023::timer;

fn difference(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    a.into_iter().filter(|item| !b.contains(item)).collect()
}

fn build_games_data(inputs: Vec<String>) -> Vec<i32> {
    let mut all_games: Vec<i32> = Vec::new();
    let mut impossible_games: Vec<i32> = Vec::new();

    for line in inputs {
        let (game_num, game_data): (&str, &str) = line.split_once(":").unwrap();
        // remove "Game " from game_num
        let game_num: &str = &game_num[5..];
        let game_num: i32 = game_num.parse().unwrap();
        all_games.push(game_num);

        let game_rounds: Vec<&str> = game_data.split(";").collect();
        for game_round in game_rounds {
            let pulls = game_round.split(",").collect::<Vec<&str>>();
            for pull in pulls {
                // 5 blue; 3 green, etc
                let (num, color) = pull.trim().split_once(" ").unwrap();
                let num = num.parse::<i32>().unwrap();
                let too_many_reds = (color == "red") && (num > 12);
                let too_many_greens = (color == "green") && (num > 13);
                let too_many_blues = (color == "blue") && (num > 14);
                if too_many_reds || too_many_greens || too_many_blues {
                    impossible_games.push(game_num);
                }
            }
        }
    }

    let possible_games = difference(all_games, impossible_games);
    possible_games
}

fn load_input() -> Vec<String> {
    let inputs = std::fs::read_to_string("../inputs/2.txt").unwrap();
    inputs.split("\n").map(|s| s.to_owned()).collect()
}

fn solve(inputs: Vec<String>) -> i32 {
    let games: Vec<i32> = build_games_data(inputs);
    games.iter().sum()
}

fn run() {
    let inputs: Vec<String> = timer! { "load_input", load_input() };
    let solution: i32 = timer! { "solve", solve(inputs) };
    dbg!(solution);
}

fn main() {
    timer! { "run", run() };
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        let inputs: Vec<String> = vec![
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        .iter()
        .map(|&s| s.to_owned())
        .collect();

        let solution = solve(inputs);

        assert_eq!(solution, 8);
    }
}
