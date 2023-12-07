use std::collections::HashMap;

use adventofcode2023::timer;

struct Card {
    id: i32,
    winning_numbers: Vec<i32>,
    numbers: Vec<i32>,
}

impl Card {
    fn new(input_str: String) -> Self {
        let data: Vec<&str> = input_str.split(":").collect();

        let id_str: &str = data[0].split_whitespace().last().unwrap();
        let id: i32 = id_str.parse().unwrap();

        let numbers: &str = &data[1];
        let number_sets: Vec<&str> = numbers.split("|").collect();

        let winning_numbers: Vec<i32> = number_sets[0]
            .trim()
            .split_whitespace()
            .filter_map(|n| n.parse().ok())
            .collect();
        let numbers: Vec<i32> = number_sets[1]
            .trim()
            .split_whitespace()
            .filter_map(|n| n.parse().ok())
            .collect();
        Card {
            id,
            winning_numbers,
            numbers,
        }
    }

    fn matching_numbers(&self) -> Vec<i32> {
        let mut matching_numbers: Vec<i32> = Vec::new();
        for num in &self.numbers {
            if self.winning_numbers.contains(num) {
                matching_numbers.push(*num);
            }
        }
        matching_numbers
    }
    // we don't need `total_score()` here, so it's removed from the 4-1 struct
}

fn solve(inputs: Vec<String>) -> i32 {
    // High-level solution logic to call additional functions as needed.
    let cards: Vec<Card> = inputs.iter().map(|x| Card::new(x.to_string())).collect();

    let mut card_counts: HashMap<i32, i32> = HashMap::new();

    for card in cards {
        if !card_counts.contains_key(&card.id) {
            card_counts.insert(card.id, 1);
        }

        let num_matching_numbers: i32 = card.matching_numbers().len() as i32;
        let mut card_copies_to_make: Vec<i32> = Vec::new();
        for i in 1..num_matching_numbers + 1 {
            card_copies_to_make.push(card.id + i);
        }

        for following_card_id in card_copies_to_make {
            if !card_counts.contains_key(&following_card_id) {
                card_counts.insert(following_card_id, 1);
            }
            // increase the count of following cards
            card_counts.insert(
                following_card_id,
                card_counts[&following_card_id] + card_counts[&card.id],
            );
        }
    }
    card_counts.values().sum()
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
    fn test_part_2() {
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

        assert_eq!(solution, 30);
    }
}
