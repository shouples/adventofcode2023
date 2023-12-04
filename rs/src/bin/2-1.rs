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
