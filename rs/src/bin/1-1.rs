use adventofcode2023::timer;

fn get_first_and_last_digits(input: &str) -> i32 {
    let mut first_digit: Option<i32> = None;
    let mut last_digit: Option<i32> = None;

    // iterate through input string to find the first digit
    for c in input.chars() {
        if c.is_digit(10) {
            first_digit = Some(c.to_digit(10).unwrap() as i32);
            break;
        }
    }

    // iterate through input string to find the last digit
    for c in input.chars().rev() {
        if c.is_digit(10) {
            last_digit = Some(c.to_digit(10).unwrap() as i32);
            break;
        }
    }

    let combined_value: String = format!(
        "{}{}",
        first_digit.unwrap().to_string(),
        last_digit.unwrap().to_string()
    );

    combined_value.parse::<i32>().unwrap()
}

fn solve(inputs: Vec<&str>) -> () {
    let values: Vec<i32> = inputs
        .iter()
        .map(|x| get_first_and_last_digits(x))
        .collect();
    let sum: i32 = values.iter().sum();
    println!("{}", sum);
}

fn run() {
    // load the puzzle input
    let inputs: String = std::fs::read_to_string("../inputs/1.txt").unwrap();
    // convert to a vector of strings
    let input_lines: Vec<&str> = inputs.split("\n").collect();
    // solve the puzzle with a timer
    timer! { solve(input_lines) };
}

fn main() {
    run();
}
