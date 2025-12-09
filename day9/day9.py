import sys


def point_in_polygon(point: tuple[int, int], polygon: list[tuple[int, int]]) -> bool:
    x, y = point
    n = len(polygon)

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        if x1 == x2:
            if x == x1 and min_y <= y <= max_y:
                return True
        elif y1 == y2:
            if y == y1 and min_x <= x <= max_x:
                return True

    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside


def does_edge_cross_rectangle_interior(
    edge_p1, edge_p2, rect_min_x, rect_max_x, rect_min_y, rect_max_y
):
    x1, y1 = edge_p1
    x2, y2 = edge_p2

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    if y1 == y2:
        if rect_min_y < y1 < rect_max_y:
            if not (x2 < rect_min_x or x1 > rect_max_x):
                overlap_start = max(x1, rect_min_x)
                overlap_end = min(x2, rect_max_x)

                if overlap_start < overlap_end:
                    return True

    elif x1 == x2:
        if rect_min_x < x1 < rect_max_x:
            if not (y2 < rect_min_y or y1 > rect_max_y):
                overlap_start = max(y1, rect_min_y)
                overlap_end = min(y2, rect_max_y)

                if overlap_start < overlap_end:
                    return True

    return False


def rectangle_fully_in_polygon(
    p1: tuple[int, int], p2: tuple[int, int], polygon: list[tuple[int, int]]
) -> bool:
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])

    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]

    for corner in corners:
        if not point_in_polygon(corner, polygon):
            return False

    for vertex in polygon:
        vx, vy = vertex
        if min_x < vx < max_x and min_y < vy < max_y:
            return False

    n = len(polygon)
    for i in range(n):
        edge_p1 = polygon[i]
        edge_p2 = polygon[(i + 1) % n]
        if does_edge_cross_rectangle_interior(
            edge_p1, edge_p2, min_x, max_x, min_y, max_y
        ):
            return False

    return True


content = sys.stdin.read()
lines = content.splitlines()

points: list[tuple[int, int]] = [
    tuple(int(x) for x in line.split(",")) for line in lines
]  # type: ignore

p1total = 0
p2total = 0

candidates = []
for i, p1 in enumerate(points):
    for p2 in points[i + 1 :]:
        x = abs(p2[0] - p1[0]) + 1
        y = abs(p2[1] - p1[1]) + 1

        area = x * y

        if area > p1total:
            p1total = area

        candidates.append((area, p1, p2))

for area, p1, p2 in sorted(candidates, reverse=True):
    if rectangle_fully_in_polygon(p1, p2, points):
        p2total = area
        break

print(f"{p1total = }")
print(f"{p2total = }")
