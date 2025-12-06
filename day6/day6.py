import sys
from collections import defaultdict

p1total = 0
p2total = 0

problems: dict[int, list[str]] = defaultdict(lambda: list())

content: str = sys.stdin.read()
content_lines = content.splitlines()

for line in content_lines:
    parts = line.split()
    for i, p in enumerate(parts):
        problems[i].append(p)

for p in problems.values():
    p1total += eval(p[-1].join(p[:-1]))

last_problem: list[str] = []

for x in range(len(content_lines[0]) - 1, -1, -1):
    all_space = True
    line = ""
    for y in range(len(content_lines)):
        if content_lines[y][x] != " ":
            all_space = False
            line += content_lines[y][x]

    last_problem.append(line)
    if all_space or x == 0:
        last_problem = [x for x in last_problem if x != ""]
        op = last_problem[-1][-1]
        val = eval(op.join(last_problem)[:-1])
        p2total += val
        last_problem = []

print(f"{p1total = }")
print(f"{p2total = }")
