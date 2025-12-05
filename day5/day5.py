import sys

RANGES = 0
ITEMS = 1

mode = RANGES

p1total = 0

ranges: list[range] = []

for line in sys.stdin.readlines():
    line = line.strip()

    if mode == RANGES:
        if len(line) == 0:
            mode = ITEMS
            continue

        parts = [int(x) for x in line.split("-")]
        ranges.append(range(parts[0], parts[1] + 1))

    elif mode == ITEMS:
        item = int(line)
        if any(item in r for r in ranges):
            p1total += 1

removed_any = True
while removed_any:
    removed_any = False

    for i in range(len(ranges) - 1):
        for j in range(i + 1, len(ranges)):
            if ranges[i].stop >= ranges[j].start and ranges[j].stop >= ranges[i].start:
                ranges[i] = range(
                    min(ranges[i].start, ranges[j].start),
                    max(ranges[i].stop, ranges[j].stop),
                )
                del ranges[j]
                removed_any = True
                break
        if removed_any:
            break


p2total = sum(r.stop - r.start for r in ranges)

print(f"{p1total = }")
print(f"{p2total = }")
