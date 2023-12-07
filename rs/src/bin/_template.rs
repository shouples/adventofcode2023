use adventofcode2023::timer;

fn solve(input: String) -> i32 {
    // High-level solution logic to call additional functions as needed.
    1
}

fn load_input() -> String {
    // Read from an input file and handle any preprocessing.
    let input_str = std::fs::read_to_string("../inputs/1.txt").unwrap();
    // add any preprocessing here
    input_str
}

fn run() {
    let input: String = timer! { "load_input", load_input() };
    let solution: i32 = timer! { "solve", solve(input) };
    dbg!(solution);
}

fn main() {
    timer! { "run", run() };
}

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn test_part_x() {}
// }
