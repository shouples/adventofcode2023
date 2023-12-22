from solutions.utils import timer


class AgricultureMappings:
    def __init__(self, inputs: list[str]):
        # pull out the seed numbers
        self.seeds = self.gather_seeds(inputs[0])

        # configure all the mappings from
        #   seeds->soil->fertilizer->water->light->temperature->humidity->location
        self.mapping: dict = {}
        for mapping in inputs[1:]:
            mapping = mapping.split("\n")
            name = mapping[0].split(":")[0].split()[0]
            mapping = mapping[1:]
            self.mapping[name] = {}
            for line in mapping:
                vals = line.split(" ")
                dest = int(vals[0])
                source = int(vals[1])
                count = int(vals[2])
                self.mapping[name][(source, source + count - 1)] = (dest, dest + count - 1)

    def gather_seeds(self, seed_str: str) -> None:
        # "seeds: 79 14 55 13"
        seed_ids = seed_str.split(": ")[1].split(" ")
        return [int(seed) for seed in seed_ids]

    def get_updated_value_from_mapping(self, value: int, mapping_name: str) -> int:
        new_value = value
        for (start, end), (dest_start, dest_end) in self.mapping[mapping_name].items():
            if start <= value <= end:
                # source/dest ranges were adjusted by the same (count) amount,
                # so we can use that to adjust the value here
                offset = dest_start - start
                new_value = value + offset
                break
        return new_value

    def get_location_for_seed(self, seed: int) -> int:
        soil = self.get_updated_value_from_mapping(seed, mapping_name="seed-to-soil")
        fertilizer = self.get_updated_value_from_mapping(soil, mapping_name="soil-to-fertilizer")
        water = self.get_updated_value_from_mapping(fertilizer, mapping_name="fertilizer-to-water")
        light = self.get_updated_value_from_mapping(water, mapping_name="water-to-light")
        temperature = self.get_updated_value_from_mapping(
            light, mapping_name="light-to-temperature"
        )
        humidity = self.get_updated_value_from_mapping(
            temperature, mapping_name="temperature-to-humidity"
        )
        location = self.get_updated_value_from_mapping(
            humidity, mapping_name="humidity-to-location"
        )
        return location

    def get_seed_locations(self) -> dict[int, int]:
        locations = {}
        for seed in self.seeds:
            locations[seed] = self.get_location_for_seed(seed)
        return locations


@timer
def solve(inputs: list[str]) -> int:
    """High-level solution logic to call additional functions as needed."""
    agmap = AgricultureMappings(inputs)
    locations = agmap.get_seed_locations()
    return min(locations.values())


@timer
def load_input() -> list[str]:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/5.txt").read().split("\n\n")


@timer
def run() -> None:
    inputs: list[str] = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
