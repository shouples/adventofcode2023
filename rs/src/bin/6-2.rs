use adventofcode2023::timer;

fn calc_possible_acceleration(race_time: usize, race_dist: usize) -> usize {
    let mut possible_accelerations: usize = 0;
    for button_press_duration in 0..race_time {
        if button_press_duration == 0 || button_press_duration == race_time {
            // button wasn't pressed or was never released, so acceleration was 0 and distance was 0
            continue;
        }

        // button was pressed for button_press_duration ms
        let travel_duration: usize = race_time - button_press_duration;
        // button_press_duration=3 would mean we're traveling for 3mm/ms, so for the rest of the
        // time we're traveling at speed=button_press_duration mm/ms
        let distance_covered: usize = travel_duration * button_press_duration;
        if distance_covered > race_dist {
            // we beat the record, hooray
            possible_accelerations += 1;
        }
    }
    possible_accelerations
}

fn solve(time: usize, distance: usize) -> usize {
    // High-level solution logic to call additional functions as needed.
    calc_possible_acceleration(time, distance)
}

fn load_input() -> (usize, usize) {
    // Read from an input file and handle any preprocessing.
    let input_str = std::fs::read_to_string("../inputs/6.txt").unwrap();
    let inputs: Vec<String> = input_str.split("\n").map(|s| s.to_owned()).collect();
    let time: usize = inputs[0]
        .split("Time:")
        .nth(1)
        .unwrap()
        .replace(" ", "")
        .parse()
        .unwrap();
    let distance: usize = inputs[1]
        .split("Distance:")
        .nth(1)
        .unwrap()
        .replace(" ", "")
        .parse()
        .unwrap();
    (time, distance)
}

fn run() {
    let (time, distance) = timer! { "load_input", load_input() };
    let solution: usize = timer! { "solve", solve(time, distance) };
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
        let inputs: Vec<&str> = vec!["Time:      7  15   30", "Distance:  9  40  200"]
            .iter()
            .map(|s| s.to_owned())
            .collect();

        let time: usize = inputs[0]
            .split("Time:")
            .nth(1)
            .unwrap()
            .replace(" ", "")
            .parse()
            .unwrap();
        let distance: usize = inputs[1]
            .split("Distance:")
            .nth(1)
            .unwrap()
            .replace(" ", "")
            .parse()
            .unwrap();

        let solution = solve(time, distance);
        assert_eq!(solution, 71503);
    }
}
