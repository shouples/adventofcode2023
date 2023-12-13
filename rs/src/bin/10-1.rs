use adventofcode2023::timer;

#[derive(Clone, Copy, Debug)]
struct MapPosition {
    can_connect_north: bool,
    can_connect_south: bool,
    can_connect_east: bool,
    can_connect_west: bool,
    lat: i32,
    lon: i32,
}

impl MapPosition {
    fn new(lat: i32, lon: i32, north: bool, south: bool, east: bool, west: bool) -> Self {
        MapPosition {
            can_connect_north: north,
            can_connect_south: south,
            can_connect_east: east,
            can_connect_west: west,
            lat: lat,
            lon: lon,
        }
    }

    fn coords(&self) -> (i32, i32) {
        (self.lat, self.lon)
    }
}

#[derive(Clone, Copy, Debug)]
enum PositionType {
    Ground(MapPosition),
    NSPipe(MapPosition),
    WEPipe(MapPosition),
    NWPipe(MapPosition),
    NEPipe(MapPosition),
    SWPipe(MapPosition),
    SEPipe(MapPosition),
    Start(MapPosition),
}

impl PositionType {
    fn coords(&self) -> (i32, i32) {
        match self {
            PositionType::Ground(pos)
            | PositionType::WEPipe(pos)
            | PositionType::NSPipe(pos)
            | PositionType::NWPipe(pos)
            | PositionType::NEPipe(pos)
            | PositionType::SWPipe(pos)
            | PositionType::SEPipe(pos)
            | PositionType::Start(pos) => pos.coords(),
        }
    }

    fn lat(&self) -> i32 {
        self.coords().0
    }

    fn lon(&self) -> i32 {
        self.coords().1
    }

    fn can_connect_east(&self) -> bool {
        match self {
            PositionType::Ground(pos)
            | PositionType::WEPipe(pos)
            | PositionType::NSPipe(pos)
            | PositionType::NWPipe(pos)
            | PositionType::NEPipe(pos)
            | PositionType::SWPipe(pos)
            | PositionType::SEPipe(pos)
            | PositionType::Start(pos) => pos.can_connect_east,
        }
    }

    fn can_connect_west(&self) -> bool {
        match self {
            PositionType::Ground(pos)
            | PositionType::WEPipe(pos)
            | PositionType::NSPipe(pos)
            | PositionType::NWPipe(pos)
            | PositionType::NEPipe(pos)
            | PositionType::SWPipe(pos)
            | PositionType::SEPipe(pos)
            | PositionType::Start(pos) => pos.can_connect_west,
        }
    }

    fn can_connect_north(&self) -> bool {
        match self {
            PositionType::Ground(pos)
            | PositionType::WEPipe(pos)
            | PositionType::NSPipe(pos)
            | PositionType::NWPipe(pos)
            | PositionType::NEPipe(pos)
            | PositionType::SWPipe(pos)
            | PositionType::SEPipe(pos)
            | PositionType::Start(pos) => pos.can_connect_north,
        }
    }

    fn can_connect_south(&self) -> bool {
        match self {
            PositionType::Ground(pos)
            | PositionType::WEPipe(pos)
            | PositionType::NSPipe(pos)
            | PositionType::NWPipe(pos)
            | PositionType::NEPipe(pos)
            | PositionType::SWPipe(pos)
            | PositionType::SEPipe(pos)
            | PositionType::Start(pos) => pos.can_connect_south,
        }
    }
}

impl PartialEq for PositionType {
    fn eq(&self, other: &Self) -> bool {
        self.coords() == other.coords()
    }
}

// onto the logic
fn convert_to_position(pos: String, lat: i32, lon: i32) -> PositionType {
    match pos.as_str() {
        "." => PositionType::Ground(MapPosition::new(lat, lon, false, false, false, false)),
        "-" => PositionType::WEPipe(MapPosition::new(lat, lon, false, false, true, true)),
        "|" => PositionType::NSPipe(MapPosition::new(lat, lon, true, true, false, false)),
        "7" => PositionType::SWPipe(MapPosition::new(lat, lon, false, true, false, true)),
        "J" => PositionType::NWPipe(MapPosition::new(lat, lon, true, false, false, true)),
        "L" => PositionType::NEPipe(MapPosition::new(lat, lon, true, false, true, false)),
        "F" => PositionType::SEPipe(MapPosition::new(lat, lon, false, true, true, false)),
        "S" => PositionType::Start(MapPosition::new(lat, lon, true, true, true, true)),
        _ => panic!("Unknown position type: {}", pos),
    }
}

struct MapRunner {
    map_data: Vec<Vec<PositionType>>,
}

impl MapRunner {
    fn new(map: String) -> Self {
        let mut map_data: Vec<Vec<PositionType>> = Vec::new();

        let map_lines: Vec<&str> = map.split("\n").collect();
        for (lat, row) in map_lines.iter().enumerate() {
            let mut new_row: Vec<PositionType> = Vec::new();
            for (lon, pos_str) in row.chars().enumerate() {
                let obj: PositionType =
                    convert_to_position(pos_str.to_string(), lat as i32, lon as i32);
                new_row.push(obj);
            }
            map_data.push(new_row);
        }
        MapRunner { map_data: map_data }
    }

    fn north_position(&self, from_position: PositionType) -> Option<PositionType> {
        if from_position.lat() != 0 && from_position.can_connect_north() {
            let to_position: PositionType =
                self.map_data[from_position.lat() as usize - 1][from_position.lon() as usize];
            if to_position.can_connect_south() {
                return Some(to_position);
            }
        }
        None
    }

    fn south_position(&self, from_position: PositionType) -> Option<PositionType> {
        let southernmost_position: i32 = self.map_data.len() as i32 - 1;
        if from_position.lat() != southernmost_position && from_position.can_connect_south() {
            let to_position: PositionType =
                self.map_data[from_position.lat() as usize + 1][from_position.lon() as usize];
            if to_position.can_connect_north() {
                return Some(to_position);
            }
        }
        None
    }

    fn west_position(&self, from_position: PositionType) -> Option<PositionType> {
        if from_position.lon() != 0 && from_position.can_connect_west() {
            let to_position: PositionType =
                self.map_data[from_position.lat() as usize][from_position.lon() as usize - 1];
            if to_position.can_connect_east() {
                return Some(to_position);
            }
        }
        None
    }

    fn east_position(&self, from_position: PositionType) -> Option<PositionType> {
        let eastmost_position: i32 = self.map_data[from_position.lat() as usize].len() as i32 - 1;
        if from_position.lon() != eastmost_position && from_position.can_connect_east() {
            let to_position: PositionType =
                self.map_data[from_position.lat() as usize][from_position.lon() as usize + 1];
            if to_position.can_connect_west() {
                return Some(to_position);
            }
        }
        None
    }

    fn available_moves(&self, from_position: PositionType) -> Vec<PositionType> {
        let mut moves: Vec<PositionType> = Vec::new();
        if let Some(pos) = self.north_position(from_position) {
            moves.push(pos);
        }
        if let Some(pos) = self.south_position(from_position) {
            moves.push(pos);
        }
        if let Some(pos) = self.east_position(from_position) {
            moves.push(pos);
        }
        if let Some(pos) = self.west_position(from_position) {
            moves.push(pos);
        }
        moves
    }

    fn get_farthest_position_in_loop(&self) -> usize {
        let mut n_moves: usize = 0;

        // find the starting position
        let mut starting_position: Option<PositionType> = None;
        for row in &self.map_data {
            for pos in row {
                if let PositionType::Start(_) = pos {
                    starting_position = Some(pos.clone());
                    break;
                }
            }
            if starting_position.is_some() {
                break;
            }
        }

        // we know the starting position is Some, so unwrap it
        let starting_position = match starting_position {
            Some(pos) => pos,
            None => {
                panic!("somehow starting_position doesn't exist?!");
            }
        };

        let mut last_position: Option<PositionType> = None;
        let mut current_position: PositionType = starting_position.clone();

        // move from the start position until we loop back to the start position, then divide the
        // number of moves by 2 (since we want to find the midway point, which will be the furthest
        // point in the loop)
        let mut available_moves: Vec<PositionType> = self.available_moves(current_position);
        let mut num_available_moves: usize = available_moves.len();

        while num_available_moves > 0 {
            let mut filtered_available_moves: Vec<PositionType> = Vec::new();

            for pos in &available_moves {
                // compare move to the starting position, as well as the last position (if it exists)
                if pos != &current_position && pos != &starting_position {
                    if last_position.is_some() {
                        if pos != &last_position.unwrap() {
                            filtered_available_moves.push(pos.clone());
                        }
                    } else {
                        filtered_available_moves.push(pos.clone());
                    }
                }
            }
            if filtered_available_moves.len() == 0 {
                // no moves left, so we're at the end of the loop
                break;
            }

            n_moves += 1;
            last_position = Some(current_position);
            current_position = filtered_available_moves[0];

            // get the next available moves
            available_moves = self.available_moves(current_position);
            num_available_moves = available_moves.len();
        }
        (n_moves / 2) + 1
    }
}

fn solve(input_str: String) -> usize {
    // High-level solution logic to call additional functions as needed.
    let runner = MapRunner::new(input_str);
    runner.get_farthest_position_in_loop()
}

fn load_input() -> String {
    // Read from an input file and handle any preprocessing.
    let input_str = std::fs::read_to_string("../inputs/10.txt").unwrap();
    // add any preprocessing here
    input_str
}

fn run() {
    let input: String = timer! { "load_input", load_input() };
    let solution: usize = timer! { "solve", solve(input) };
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
        let input_str1: String = r#".....
.S-7.
.|.|.
.L-J.
....."#
            .to_owned();
        let solution1 = solve(input_str1);
        assert_eq!(solution1, 4);

        let input_str2: String = r#"..F7.
.FJ|.
SJ.L7
|F--J
LJ..."#
            .to_owned();
        let solution2 = solve(input_str2);
        assert_eq!(solution2, 8);
    }
}
