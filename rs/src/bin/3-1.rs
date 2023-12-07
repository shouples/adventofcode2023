use adventofcode2023::timer;

const PART_SYMBOLS: &str = "!\"#$%&'()*+,-/:;<=>?@[\\]^_`{|}~";

fn get_part_num_sum(rows: Vec<String>) -> Vec<i32> {
    let mut part_nums = Vec::new();
    let last_row_position = rows.len() - 1;

    for (i, row) in rows.iter().enumerate() {
        // flags to determine whether we can check above/below the current row
        let top_row: bool = i == 0;
        let bottom_row: bool = i == last_row_position;

        // build up a string as we find numbers in the row
        let mut checking_number = String::new();

        let last_char_position = row.len() - 1;

        for (char_index, char) in row.chars().enumerate() {
            if !char.is_digit(10) {
                checking_number.clear();
                continue;
            }

            checking_number.push(char);

            // if we're at the end of the row, or the next char isn't a digit, it's time to check
            // our checking_number against values above/below/left/right and diagonal for symbols
            let at_end_of_row = char_index == last_char_position;
            let next_char_is_not_digit =
                !row.chars().nth(char_index + 1).unwrap_or(' ').is_digit(10);
            if at_end_of_row || next_char_is_not_digit {
                let above: usize = if i > 0 { i - 1 } else { 0 };
                let below: usize = if i < last_row_position { i + 1 } else { i };
                let left: usize = char_index.saturating_sub(checking_number.len());
                let right: usize = usize::min(char_index + 1, last_char_position);

                // check all around the current number, e.g.:
                // xxxxx
                // y123y
                // zzzzz

                let mut chars_above = Vec::new();
                if !top_row {
                    chars_above = rows[above][left..=right].chars().collect();
                }

                let char_left = row.chars().nth(left).unwrap();
                let char_right = row.chars().nth(right).unwrap();

                let mut chars_below = Vec::new();
                if !bottom_row {
                    chars_below = rows[below][left..=right].chars().collect();
                }

                if PART_SYMBOLS.contains(char_left) {
                    part_nums.push(checking_number.parse::<i32>().unwrap());
                    continue;
                }

                if PART_SYMBOLS.contains(char_right) {
                    part_nums.push(checking_number.parse::<i32>().unwrap());
                    continue;
                }

                if chars_above.iter().any(|&char| PART_SYMBOLS.contains(char)) {
                    part_nums.push(checking_number.parse::<i32>().unwrap());
                    continue;
                }

                if chars_below.iter().any(|&char| PART_SYMBOLS.contains(char)) {
                    part_nums.push(checking_number.parse::<i32>().unwrap());
                    continue;
                }
            }
        }
    }

    part_nums
}

fn solve(inputs: Vec<String>) -> i32 {
    // High-level solution logic to call additional functions as needed.
    let nums: Vec<i32> = get_part_num_sum(inputs);
    nums.iter().sum()
}

fn load_input() -> Vec<String> {
    // Read from an input file and handle any preprocessing.
    let input_str: String = std::fs::read_to_string("../inputs/3.txt").unwrap();
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
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        .iter()
        .map(|&s| s.to_owned())
        .collect();

        let solution = solve(inputs);

        assert_eq!(solution, 4361);
    }
}
