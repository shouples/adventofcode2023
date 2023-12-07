use adventofcode2023::timer;

fn build_games_data(inputs: Vec<String>) -> i32 {
    let mut power_sum: i32 = 0;

    for line in inputs {
        let (_, game_data): (&str, &str) = line.split_once(":").unwrap();

        let mut required_reds: i32 = 0;
        let mut required_greens: i32 = 0;
        let mut required_blues: i32 = 0;

        let game_rounds: Vec<&str> = game_data.split(";").collect();
        for game_round in game_rounds {
            let pulls = game_round.split(",").collect::<Vec<&str>>();
            for pull in pulls {
                // 5 blue; 3 green, etc
                let (num, color) = pull.trim().split_once(" ").unwrap();
                let num = num.parse::<i32>().unwrap();
                match color {
                    "red" => {
                        if required_reds < num {
                            required_reds = num;
                        }
                    }
                    "green" => {
                        if required_greens < num {
                            required_greens = num;
                        }
                    }
                    "blue" => {
                        if required_blues < num {
                            required_blues = num;
                        }
                    }
                    _ => panic!("unexpected color"),
                }
            }
        }

        power_sum += required_reds * required_greens * required_blues;
    }
    power_sum
}

fn load_input() -> Vec<String> {
    let inputs = std::fs::read_to_string("../inputs/2.txt").unwrap();
    inputs.split("\n").map(|s| s.to_owned()).collect()
}

fn solve(inputs: Vec<String>) -> i32 {
    return build_games_data(inputs);
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
    fn test_part_2() {
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

        assert_eq!(solution, 2286);
    }
}
