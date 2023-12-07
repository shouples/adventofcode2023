use adventofcode2023::timer;

struct Card {
    winning_numbers: Vec<i32>,
    numbers: Vec<i32>,
}

impl Card {
    fn new(input_str: String) -> Self {
        let data: Vec<&str> = input_str.split(":").collect();

        let numbers: &str = &data[1];
        let number_sets: Vec<&str> = numbers.split("|").map(|s| s.trim()).collect();

        let winning_numbers: Vec<i32> = number_sets[0]
            .split_whitespace()
            .filter_map(|n| n.parse().ok())
            .collect();
        let numbers: Vec<i32> = number_sets[1]
            .split_whitespace()
            .filter_map(|n| n.parse().ok())
            .collect();
        Card {
            winning_numbers,
            numbers,
        }
    }

    fn matching_numbers(&self) -> Vec<i32> {
        let matching_numbers: Vec<i32> = self
            .numbers
            .iter()
            .filter(|&&x| self.winning_numbers.contains(&x))
            .cloned()
            .collect();
        matching_numbers
    }

    fn total_score(&self) -> i32 {
        let matches = &self.matching_numbers();
        if matches.is_empty() {
            return 0;
        }

        let mut score: i32 = 0;
        for (i, _) in matches.iter().enumerate() {
            if i == 0 {
                score = 1
            } else {
                score *= 2;
            }
        }
        score
    }
}

fn solve(inputs: Vec<String>) -> i32 {
    // High-level solution logic to call additional functions as needed.
    inputs
        .iter()
        .map(|input| Card::new(input.to_string()).total_score())
        .sum()
}

fn load_input() -> Vec<String> {
    // Read from an input file and handle any preprocessing.
    let input_str = std::fs::read_to_string("../inputs/4.txt").unwrap();
    // add any preprocessing here
    input_str.split("\n").map(|s| s.to_owned()).collect()
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
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        .iter()
        .map(|&s| s.to_owned())
        .collect();

        let solution: i32 = solve(inputs);

        assert_eq!(solution, 13);
    }
}
