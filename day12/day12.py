import sys
from dataclasses import dataclass


class Shape:
    def __init__(self, blocks: tuple[tuple[int, ...], ...]):
        self.blocks = blocks

        self.filled_positions: list[tuple[int, int]] = []
        for r, row in enumerate(blocks):
            for c, val in enumerate(row):
                if val == 1:
                    self.filled_positions.append((r, c))

        self.filled_count = len(self.filled_positions)


@dataclass
class Area:
    width: int
    height: int
    counts: tuple[int, ...]


def can_fit_shapes(area: Area, shapes: list[Shape]) -> bool:
    shapes_to_place: list[Shape] = []
    for i, count in enumerate(area.counts):
        for _ in range(count):
            shapes_to_place.append(shapes[i])

    total_filled = sum(s.filled_count for s in shapes_to_place)
    total_area = area.width * area.height
    return total_area >= total_filled


content = sys.stdin.read()
*presents_lines, areas_lines = content.split("\n\n")

presents: list[Shape] = []
for present_lines in presents_lines:
    present_lines = present_lines.splitlines()[1:]
    blocks: tuple[tuple[int, ...], ...] = tuple(
        tuple(
            1 if present_lines[y][x] == "#" else 0 for x in range(len(present_lines[y]))
        )
        for y in range(len(present_lines))
    )
    presents.append(Shape(blocks))

areas: list[Area] = []
for line in areas_lines.splitlines():
    dims_combined, counts = line.split(": ")
    dims: list[str] = dims_combined.split("x")
    counts = counts.split(" ")
    areas.append(Area(int(dims[0]), int(dims[1]), tuple(map(int, counts))))

p1total = 0
for area in areas:
    if can_fit_shapes(area, presents):
        p1total += 1

print(f"{p1total = }")
