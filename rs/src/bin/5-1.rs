use std::collections::HashMap;

use adventofcode2023::timer;

struct AgricultureMappings {
    seeds: Vec<String>,
    mapping: HashMap<String, HashMap<(i64, i64), (i64, i64)>>,
}

fn gather_seeds(seed_str: String) -> Vec<String> {
    let seeds: Vec<String> = seed_str
        .split(": ")
        .nth(1)
        .unwrap()
        .split_whitespace()
        .map(|x| x.to_string())
        .collect();
    seeds
}

impl AgricultureMappings {
    fn new(inputs: Vec<String>) -> Self {
        let seeds = gather_seeds(inputs[0].to_string());
        let mut full_mapping: HashMap<String, HashMap<(i64, i64), (i64, i64)>> = HashMap::new();
        for mapping in &inputs[1..] {
            let mapping: Vec<&str> = mapping.split("\n").collect();
            let mapping_name: String = mapping[0]
                .split(":")
                .nth(0)
                .unwrap()
                .split_whitespace()
                .nth(0)
                .unwrap()
                .to_owned();
            let mapping_data: Vec<&str> = mapping[1..].to_vec();
            // create the data for the individual conversions (seed->soil, soil->fertilizer, etc)
            let mut conversion_mapping: HashMap<(i64, i64), (i64, i64)> = HashMap::new();
            for line in mapping_data {
                let values: Vec<&str> = line.split_whitespace().collect();
                let dest: i64 = values[0].parse().unwrap();
                let source: i64 = values[1].parse().unwrap();
                let count: i64 = values[2].parse().unwrap();
                conversion_mapping.insert((source, source + count - 1), (dest, dest + count - 1));
            }
            full_mapping.insert(mapping_name, conversion_mapping);
        }
        AgricultureMappings {
            seeds: seeds,
            mapping: full_mapping,
        }
    }

    fn get_updated_value_from_mapping(&self, value: i64, mapping_name: &str) -> i64 {
        let mut new_value = value;
        for ((start, end), (dest_start, _)) in &self.mapping[mapping_name] {
            if (start <= &value) && (value <= *end) {
                let offset = dest_start - start;
                new_value = value + offset;
                break;
            }
        }

        new_value
    }

    fn get_location_for_seed(&self, seed_id: i64) -> i64 {
        let soil: i64 = self.get_updated_value_from_mapping(seed_id, "seed-to-soil");
        let fertilizer: i64 = self.get_updated_value_from_mapping(soil, "soil-to-fertilizer");
        let water: i64 = self.get_updated_value_from_mapping(fertilizer, "fertilizer-to-water");
        let sunlight: i64 = self.get_updated_value_from_mapping(water, "water-to-light");
        let temperature: i64 =
            self.get_updated_value_from_mapping(sunlight, "light-to-temperature");
        let humidity: i64 =
            self.get_updated_value_from_mapping(temperature, "temperature-to-humidity");
        let location: i64 = self.get_updated_value_from_mapping(humidity, "humidity-to-location");
        location
    }

    fn get_seed_locations(&self) -> HashMap<i64, i64> {
        let mut locations: HashMap<i64, i64> = HashMap::new();
        for seed in &self.seeds {
            let seed_id: i64 = seed.parse().unwrap();
            let location: i64 = self.get_location_for_seed(seed_id);
            locations.insert(seed_id, location);
        }
        locations
    }
}

fn solve(inputs: Vec<String>) -> i64 {
    let agmap: AgricultureMappings = AgricultureMappings::new(inputs);
    let locations: HashMap<i64, i64> = agmap.get_seed_locations();
    locations.values().min().unwrap().to_owned()
}

fn load_input() -> Vec<String> {
    let input_str = std::fs::read_to_string("../inputs/5.txt").unwrap();
    let inputs: Vec<String> = input_str.split("\n\n").map(|s| s.to_owned()).collect();
    inputs
}

fn run() {
    let inputs: Vec<String> = timer! { "load_input", load_input() };
    let solution: i64 = timer! { "solve", solve(inputs) };
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
        let inputs: Vec<String> = "seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"
            .split("\n\n")
            .map(|s| s.to_owned())
            .collect();

        let solution: i64 = solve(inputs);

        assert_eq!(solution, 35);
    }
}
