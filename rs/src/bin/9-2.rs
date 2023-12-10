use adventofcode2023::timer;

fn predict_next(readings: Vec<i32>) -> i32 {
    let mut diffs: Vec<i32> = Vec::new();

    for (i, reading) in readings.iter().enumerate() {
        if i == readings.len() - 1 {
            // at the last reading, can't subtract the next reading
            break;
        }
        // get the difference between the current reading and the next reading
        let next_reading: i32 = readings[i + 1];
        let diff: i32 = next_reading - reading;
        diffs.push(diff);
    }

    // if any of the diffs are different, return the last reading + the diff
    if !diffs.iter().all(|&x| x == 0) {
        return readings.last().unwrap() + predict_next(diffs);
    }

    readings.last().unwrap() + diffs[0]
}
fn solve(inputs: Vec<Vec<i32>>) -> i32 {
    // High-level solution logic to call additional functions as needed.
    let mut next_readings: Vec<i32> = Vec::new();
    for readings in inputs {
        // reverse the order so we're predicting what came before the first one, rather than
        // predicting what comes after the last one (from part 1)
        let reversed_readings: Vec<i32> = readings.iter().rev().cloned().collect();
        let next_reading: i32 = predict_next(reversed_readings);
        next_readings.push(next_reading);
    }
    next_readings.iter().sum()
}

fn load_input() -> Vec<Vec<i32>> {
    // Read from an input file and handle any preprocessing.
    let input_str = std::fs::read_to_string("../inputs/9.txt").unwrap();

    let readings: Vec<Vec<i32>> = input_str
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect()
        })
        .collect();
    readings
}

fn run() {
    let input: Vec<Vec<i32>> = timer! { "load_input", load_input() };
    let solution: i32 = timer! { "solve", solve(input) };
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
        let inputs: Vec<String> = vec!["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]
            .iter()
            .map(|&s| s.to_owned())
            .collect();
        let readings: Vec<Vec<i32>> = inputs
            .iter()
            .map(|line| {
                line.split_whitespace()
                    .map(|x| x.parse::<i32>().unwrap())
                    .collect()
            })
            .collect();

        let solution: i32 = solve(readings);

        assert_eq!(solution, 2);
    }
}
