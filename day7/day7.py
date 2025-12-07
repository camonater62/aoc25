import sys

p1total = 0

lines = sys.stdin.read().splitlines()

beams: set[int] = {lines[0].index("S")}
for line in lines[1:]:
    new_beams: set[int] = set()

    for b in beams:
        if line[b] == "^":
            new_beams.add(b - 1)
            new_beams.add(b + 1)
            p1total += 1
        else:
            new_beams.add(b)

    beams = new_beams

grid = [[0 for _ in range(len(line))] for line in lines]
grid[0][lines[0].index("S")] = 1

for y in range(len(grid) - 1):
    for x in range(len(grid[y])):
        if lines[y][x] == "^":
            grid[y + 1][x - 1] += grid[y][x]
            grid[y + 1][x + 1] += grid[y][x]
        else:
            grid[y + 1][x] += grid[y][x]

p2total = sum(grid[-1])

print(f"{p1total = }")
print(f"{p2total = }")
