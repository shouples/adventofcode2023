from solutions import day15_1, day15_2


def test_part1():
    inputs = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

    assert day15_1.solve(inputs) == 1320


def test_part2():
    inputs = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

    assert day15_2.solve(inputs) == 145
