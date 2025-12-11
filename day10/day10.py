import sys
from dataclasses import dataclass
import numpy as np
from scipy.optimize import linprog
from math import ceil


p1total = 0
p2total = 0

content = sys.stdin.read()
lines = content.splitlines()


@dataclass
class MachineState:
    state: tuple[bool, ...]
    num_presses: int = 0


def solve_machine(desired_state: tuple[bool, ...], buttons: list[list[int]]):
    Q = [MachineState(tuple([False] * len(desired_state)))]

    visited_states = set()

    while len(Q) > 0:
        front = Q.pop(0)

        if front.state == desired_state:
            return front.num_presses

        if front.state in visited_states:
            continue

        visited_states.add(front.state)

        for b in buttons:
            new_state = list(front.state)
            for i in b:
                new_state[i] = not new_state[i]
            Q.append(MachineState(tuple(new_state), front.num_presses + 1))

    return 0


for line in lines:
    parts = line.split(" ")
    desired_state = [(c == "#") for c in parts[0][1:-1]]
    buttons = [p[1:-1] for p in parts[1:-1]]
    buttons = [list(int(x) for x in p.split(",")) for p in buttons]
    joltages = list(int(x) for x in parts[-1][1:-1].split(","))

    p1total += solve_machine(tuple(desired_state), buttons)

    cost_per_button = np.ones(len(buttons))
    constraint_matrix = np.zeros((len(joltages), len(buttons)))
    target_values = np.array(joltages)

    for joltage in range(len(joltages)):
        for i, button in enumerate(buttons):
            if joltage in button:
                constraint_matrix[joltage][i] = 1

    res = linprog(
        cost_per_button,
        A_eq=constraint_matrix,
        b_eq=target_values,
        method="highs",
        integrality=True,
    )

    p2total += ceil(res.fun)


print(f"{p1total = }")
print(f"{p2total = }")
