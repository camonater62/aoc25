import sys

pos = 50
p1count = 0
p2count = 0

for line in sys.stdin.readlines():
    line = line.strip()

    direction = line[0]
    amount = int(line[1:])

    if direction == "L":
        for _ in range(amount):
            pos = (pos - 1 + 100) % 100
            if pos == 0:
                p2count += 1
    elif direction == "R":
        for _ in range(amount):
            pos = (pos + 1) % 100
            if pos == 0:
                p2count += 1

    if pos == 0:
        p1count += 1

print(f"{p1count = }")
print(f"{p2count = }")
