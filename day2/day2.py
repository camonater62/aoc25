import sys

id_ranges = sys.stdin.read().strip().split(",")

p1total = 0
p2total = 0

for idr in id_ranges:
    start, end = [int(x) for x in idr.strip().split("-")]

    print(f"{start = }, {end = } => {end - start + 1}")

    for i in range(start, end + 1):
        s = str(i)
        l = len(s)

        for ii in range(2, l + 1):
            if l % ii == 0:
                width = l // ii
                parts = [s[x * width : (x + 1) * width] for x in range(ii)]
                if len(set(parts)) == 1:
                    print(s)
                    p2total += i
                    if ii == 2:
                        p1total += i
                    break


print(f"{p1total = }")
print(f"{p2total = }")
