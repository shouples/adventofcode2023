# Advent of Code 2023

Getting into the holiday spirit with [Advent of Code](https://adventofcode.com/2023) puzzles, this year in Python and Rust*! 🐍🦀☃️🎁

There are three main sections below for each day's puzzle, with two icons/emojis representing parts 1 and 2:

 - the exploration/notebook solution(s) for each part
 - the executable Python for each part (`poetry run ./solutions/day____.py`)
 - the executable Rust for each part (`cargo run --bin ____ --release`)
 
For the non-notebook sections, tests (`pytest` and `cargo nextest`) are be included for any with a ✅ to ensure the solutions work with the example inputs provided in each day of Advent of Code puzzle.

| Key | |
| -- | -- |
| ✅ | done |
| 🕒| to do |
|❔| unreleased |
| ⛔ | admitted defeat |

| Day       | Notebook 📓 | Python 🐍  | Rust 🦀     | Notes |
|-----------|-------------|-------------|-------------|-------|
| 1   | ✅✅  | ✅✅  | ✅✅ | |
| 2   | ✅✅  | ✅✅  | ✅✅ | |
| 3   | ✅✅  | ✅✅  | ✅✅ | |
| 4   | ✅✅  | ✅✅  | ✅✅ | |
| 5   | ✅⛔  | ✅⛔  | ✅⛔ | I'm having a hard time wrapping my head around what part 2 is asking, even after seeing some visualizations. |
| 6   | ✅✅  | ✅✅  | ✅✅ | |
| 7   | ✅✅  | ✅✅  | ✅✅ | I haven't had to deal with rust's `Display` impl for custom `fmt` until now, but it helped debugging quite a bit here; it wasn't as clean/straightforward as python's `__repr__` method, but still useful to play with. |
| 8   | ✅🕒  | ✅🕒  | 🕒🕒 | Initially abandoned part 2, but I think I was on the right track (not brute-forcing) and want to revisit it. |
| 9   | ✅✅  | ✅✅  | ✅✅ | |
| 10   | ✅⛔  | ✅⛔ | ✅⛔ | |
| 11   | ✅✅  | ✅✅ | 🕒🕒 | |
| 12   | ✅⛔  | ✅⛔  | 🕒🕒 | Getting pretty tired of the "do part 1 but with way more data" trend here. |
| 13   | ✅⛔  | ✅⛔  | 🕒🕒 | Multiple examples were working in part 2, but something isn't quite working correctly on the actual inputs. |
| 14   | ✅⛔  | ✅⛔ | 🕒🕒 | |
| 15   | ✅✅  | ✅✅ | 🕒🕒 | This was a nice little break compared to the past week's puzzle offerings. |
| 16   | ✅✅  | ✅✅ | 🕒🕒 | |
| 17   | ✅⛔  | ✅⛔ | 🕒🕒 | Same issue as day 13 with part 2 here. |
| 18   | ✅✅  | ✅✅ | 🕒🕒 | |
| 19   | ✅⛔  | ✅⛔ | 🕒🕒 | |
| 20   | 🕒🕒  | 🕒🕒 | 🕒🕒 | |
| 21   | 🕒🕒  | 🕒🕒 | 🕒🕒 | |
| 22   | ⛔⛔  | ⛔⛔ | ⛔⛔ | Example passed, real input kept being flagged as too high. |
| 23   | ❔❔  | ❔❔ | ❔❔ | |
| 24   | ❔❔  | ❔❔ | ❔❔ | |
| 25   | ❔❔  | ❔❔ | ❔❔ | |

_*I'm starting with Python each day, and using this year as a way to become generally more comfortable with Rust. Maybe I'll start puzzles in Rust next year!_