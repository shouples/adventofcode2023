use adventofcode2023::timer;
use std::collections::HashMap;

fn get_first_and_last_digits_with_conversion(line: &str) -> i32 {
    let digit_conversions: HashMap<String, i32> = HashMap::from([
        ("zero".to_string(), 0),
        ("one".to_string(), 1),
        ("two".to_string(), 2),
        ("three".to_string(), 3),
        ("four".to_string(), 4),
        ("five".to_string(), 5),
        ("six".to_string(), 6),
        ("seven".to_string(), 7),
        ("eight".to_string(), 8),
        ("nine".to_string(), 9),
    ]);

    let mut first_digit: Option<i32> = None;
    let mut last_digit: Option<i32> = None;

    // iterate through input string to find the first digit
    for (i, c) in line.chars().enumerate() {
        if first_digit.is_some() {
            break;
        }
        if c.is_digit(10) {
            first_digit = Some(c.to_digit(10).unwrap() as i32);
            break;
        }
        for (str_digit, digit) in digit_conversions.iter() {
            if line[i..].starts_with(str_digit) {
                first_digit = Some(*digit);
                break;
            }
        }
    }

    // iterate through input string to find the last digit
    for (i, c) in line.chars().rev().enumerate() {
        if last_digit.is_some() {
            break;
        }
        if c.is_digit(10) {
            last_digit = Some(c.to_digit(10).unwrap() as i32);
            break;
        }
        for (str_digit, digit) in digit_conversions.iter() {
            if line[..line.len() - i].ends_with(str_digit) {
                last_digit = Some(*digit);
                break;
            }
        }
    }

    let combined_value: String = format!(
        "{}{}",
        first_digit.unwrap().to_string(),
        last_digit.unwrap().to_string()
    );

    combined_value.parse::<i32>().unwrap()
}

fn load_input() -> Vec<String> {
    let inputs = std::fs::read_to_string("../inputs/1.txt").unwrap();
    inputs.split("\n").map(|s| s.to_owned()).collect()
}

fn solve(inputs: Vec<String>) -> () {
    let values: Vec<i32> = inputs
        .iter()
        .map(|x| get_first_and_last_digits_with_conversion(x))
        .collect();
    let sum: i32 = values.iter().sum();
    println!("{}", sum);
}

fn run() {
    let inputs: Vec<String> = timer! { "load_input", load_input() };
    timer! { "solve", solve(inputs) };
}

fn main() {
    timer! { "run", run() };
}
