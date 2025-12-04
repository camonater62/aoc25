import sys
import copy

p1total = 0
p2total = 0

grid: list[list[str]] = []

for line in sys.stdin.readlines():
    line = line.strip()
    grid.append([c for c in line])

next_grid = copy.deepcopy(grid)

removed_some = True

while removed_some:
    num_removed = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                num = 0

                for oy in range(-1, 2):
                    for ox in range(-1, 2):
                        if oy == ox and ox == 0:
                            continue

                        cy = y + oy
                        cx = x + ox

                        if cy == -1 or cy >= len(grid):
                            continue
                        if cx == -1 or cx >= len(grid[cy]):
                            continue

                        if grid[cy][cx] == "@":
                            num += 1

                if num < 4:
                    num_removed += 1
                    next_grid[y][x] = "."
                else:
                    next_grid[y][x] = grid[y][x]
            else:
                next_grid[y][x] = grid[y][x]

    removed_some = num_removed > 0

    if p1total == 0:
        p1total = num_removed

    p2total += num_removed

    grid = copy.deepcopy(next_grid)

print(f"{p1total = }")
print(f"{p2total = }")
