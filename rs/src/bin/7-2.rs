use std::collections::{HashMap, HashSet};
use std::fmt::Display;

use adventofcode2023::timer;

const CARD_RANKS_WITH_JOKERS: &str = "J23456789TQKA";

#[derive(Debug)]
struct Card {
    value: char,
}

impl Card {
    fn new(value: char) -> Card {
        Card { value }
    }

    fn score(&self) -> usize {
        CARD_RANKS_WITH_JOKERS
            .chars()
            .position(|r| r == self.value)
            .unwrap()
    }
}

impl Display for Card {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

#[derive(Debug)]
struct CardHandWithJokers {
    bid: usize,
    cards: Vec<Card>,
}

impl CardHandWithJokers {
    fn new(bid: usize, raw_cards: Vec<char>) -> CardHandWithJokers {
        let cards = raw_cards.iter().map(|c| Card::new(*c)).collect();
        CardHandWithJokers { bid, cards }
    }

    fn card_counts(&self) -> HashMap<char, u32> {
        let mut card_counts: HashMap<char, u32> = HashMap::new();

        for card in self.cards.iter() {
            let count = card_counts.entry(card.value).or_insert(0);
            *count += 1;
        }

        // adjust counts for the number of jokers present
        let joker_count: usize = card_counts.remove(&'J').unwrap_or(0) as usize;
        if joker_count == 0 {
            return card_counts;
        }

        // remove jokers from card_counts
        if joker_count == 5 {
            // all jokers, max score
            card_counts = HashMap::from([('A', 5)]);
        } else if joker_count > 0 {
            // some number of jokers are present, find out how to apply them to the top-counted card
            let top_card_count: usize = card_counts.values().max().unwrap().clone() as usize;
            let top_count_cards: Vec<char> = card_counts
                .iter()
                .filter(|&(&card, &count)| count == top_card_count as u32 && card != 'J')
                .map(|(&card, _)| card)
                .collect();
            if top_count_cards.len() == 1 {
                // one non-joker card is the top count, add jokers to it
                let top_count_card = top_count_cards[0];
                let new_count = top_card_count + joker_count;
                card_counts.insert(top_count_card, new_count as u32);
            } else {
                // multiple top count cards, add jokers to the highest value card
                let unique_top_cards: HashSet<char> = top_count_cards.into_iter().collect();
                let higher_card: char = unique_top_cards
                    .iter()
                    .max_by(|&a, &b| {
                        CARD_RANKS_WITH_JOKERS
                            .find(*a)
                            .cmp(&CARD_RANKS_WITH_JOKERS.find(*b))
                    })
                    .unwrap()
                    .clone();
                let new_count = top_card_count + joker_count;
                card_counts.insert(higher_card, new_count as u32);
            }
        }
        card_counts
    }

    fn one_pair(&self) -> bool {
        self.card_counts()
            .values()
            .filter(|&count| *count == 2)
            .count()
            == 1
    }

    fn two_pairs(&self) -> bool {
        self.card_counts()
            .values()
            .filter(|&count| *count == 2)
            .count()
            == 2
    }

    fn three_of_a_kind(&self) -> bool {
        self.card_counts()
            .values()
            .filter(|&count| *count == 3)
            .count()
            == 1
    }

    fn full_house(&self) -> bool {
        self.one_pair() && self.three_of_a_kind()
    }

    fn four_of_a_kind(&self) -> bool {
        self.card_counts()
            .values()
            .filter(|&count| *count == 4)
            .count()
            == 1
    }

    fn five_of_a_kind(&self) -> bool {
        self.card_counts()
            .values()
            .filter(|&count| *count == 5)
            .count()
            == 1
    }

    fn rank(&self) -> String {
        if self.five_of_a_kind() {
            return "5K".to_string();
        } else if self.four_of_a_kind() {
            return "4K".to_string();
        } else if self.full_house() {
            return "FH".to_string();
        } else if self.three_of_a_kind() {
            return "3K".to_string();
        } else if self.two_pairs() {
            return "2P".to_string();
        } else if self.one_pair() {
            return "1P".to_string();
        }
        "HK".to_string()
    }

    fn rank_score(&self) -> usize {
        let mut total_hand_score: usize = 0;

        let hand_ranks = vec!["HC", "1P", "2P", "3K", "FH", "4K", "5K"];
        total_hand_score += hand_ranks.iter().position(|&r| r == self.rank()).unwrap() * 1000000000;
        total_hand_score += self.cards.iter().nth(0).unwrap().score() * 10000000;
        total_hand_score += self.cards.iter().nth(1).unwrap().score() * 100000;
        total_hand_score += self.cards.iter().nth(2).unwrap().score() * 1000;
        total_hand_score += self.cards.iter().nth(3).unwrap().score() * 10;
        total_hand_score += self.cards.iter().nth(4).unwrap().score();
        total_hand_score
    }
}

impl Display for CardHandWithJokers {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        // create a quick string repr of the card values
        let mut cards_str = String::new();
        for card in self.cards.iter() {
            cards_str.push_str(&card.to_string());
        }
        write!(
            f,
            "<CardHandWithJokers {}: {} (score={})",
            cards_str,
            self.rank(),
            self.rank_score()
        )
    }
}

fn calculate_winnings(hands: Vec<CardHandWithJokers>) -> usize {
    let mut winnings = 0;
    for (rank, hand) in hands.iter().enumerate() {
        let rank_multiplier = rank + 1;
        let hand_winning = hand.bid * rank_multiplier;
        winnings += hand_winning;
    }
    winnings
}

fn solve(input: Vec<String>) -> usize {
    // High-level solution logic to call additional functions as needed.
    let mut hands = Vec::new();
    for line in input {
        let hand_bid: Vec<&str> = line.split_whitespace().collect();
        let cards: Vec<char> = hand_bid[0].chars().collect();
        let bid: usize = hand_bid[1].parse().unwrap();
        hands.push(CardHandWithJokers::new(bid, cards));
    }
    hands.sort_by(|a, b| a.rank_score().cmp(&b.rank_score()));

    for hand in hands.iter() {
        println!("{}", hand);
    }

    let winnings = calculate_winnings(hands);
    winnings
}

fn load_input() -> Vec<String> {
    // Read from an input file and handle any preprocessing.
    let input_str = std::fs::read_to_string("../inputs/7.txt").unwrap();
    let inputs: Vec<String> = input_str.split("\n").map(|s| s.to_owned()).collect();
    inputs
}

fn run() {
    let inputs: Vec<String> = timer! { "load_input", load_input() };
    let solution: usize = timer! { "solve", solve(inputs) };
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
        let inputs = vec![
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ]
        .iter()
        .map(|s| s.to_string())
        .collect();
        let solution: usize = solve(inputs);
        assert_eq!(solution, 5905);
    }
}
