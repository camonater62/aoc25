import sys
import itertools
import math
import functools

p1total = 0
p2total = 0

content = sys.stdin.read()
lines = content.splitlines()

coords: list[tuple[int, int, int]] = []

for line in lines:
    coord: tuple[int, int, int] = tuple(int(x) for x in line.split(","))  # type: ignore
    coords.append(coord)

pairs_by_dist = sorted(
    itertools.combinations(coords, 2), key=lambda x: math.dist(x[0], x[1])
)

circuits: list[set[tuple[int, int, int]]] = list({c} for c in coords)

for i, p in enumerate(pairs_by_dist):
    if i == 1000:
        p1total = functools.reduce(
            lambda a, b: a * b, sorted([len(c) for c in circuits], reverse=True)[:3]
        )

    p0c = -1
    p1c = -1
    for ci, c in enumerate(circuits):
        if p[0] in c:
            p0c = ci
        if p[1] in c:
            p1c = ci

    if p0c == p1c:
        continue

    for p1p in circuits[p1c]:
        circuits[p0c].add(p1p)
    del circuits[p1c]

    if len(circuits) == 1:
        p2total = p[0][0] * p[1][0]
        break

print(f"{p1total = }")
print(f"{p2total = }")
