from dataclasses import dataclass

from solutions.utils import timer


@dataclass
class Rating:
    x: int
    m: int
    a: int
    s: int

    @property
    def score(self) -> int:
        return self.x + self.m + self.a + self.s


def parse_workflows(workflows) -> dict:
    workflow_rules = {}
    for workflow in workflows:
        workflow_name, workflow_rules_str = workflow.split("{")
        workflow_rules_str = workflow_rules_str[:-1]
        workflow_rules[workflow_name] = workflow_rules_str.split(",")
    return workflow_rules


def run_workflow(rating: Rating, workflows: dict, workflow_name: str = None) -> int:
    workflow_name = workflow_name or "in"
    if workflow_name == "R":
        return 0
    if workflow_name == "A":
        return rating.score

    workflow = workflows[workflow_name]
    # {"tq": ["x<2961:A", "m<1415:A", "A"]}
    for i, rule in enumerate(workflow):
        if ":" in rule:
            rule, next_workflow_name = rule.split(":")
            # evaluate something like `rating.s<1453`
            if eval(f"rating.{rule}"):
                return run_workflow(rating, workflows, next_workflow_name)
            else:
                continue
        else:
            return run_workflow(rating, workflows, rule)


def run_workflow_rules(workflows: list[str], ratings: list[str]) -> int:
    workflow_rules: dict = parse_workflows(workflows)
    score = 0
    for rating in ratings:
        rating_obj = Rating(*[int(value.split("=")[1]) for value in rating.strip("{}").split(",")])
        result: int = run_workflow(rating_obj, workflow_rules)
        score += result
    return score


@timer
def solve(inputs: str) -> int:
    """High-level solution logic to call additional functions as needed."""
    workflows, ratings = inputs.split("\n\n")
    result = run_workflow_rules(workflows.split("\n"), ratings.split("\n"))
    return result


@timer
def load_input() -> str:
    """Read from an input file and handle any preprocessing."""
    return open("../inputs/19.txt").read()


@timer
def run() -> None:
    inputs: str = load_input()
    solution = solve(inputs)
    print(f"{solution=}")


if __name__ == "__main__":
    run()
