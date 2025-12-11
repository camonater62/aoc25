import sys
import functools

p1total = 0
p2total = 0

content = sys.stdin.read()
lines = content.splitlines()

connections: dict[str, tuple[str]] = dict()

for line in lines:
    node, *out = line.split()
    node = node[:-1]
    connections[node] = tuple(out)  # type: ignore


def search(node: str):
    if node == "out":
        return 1

    return sum(search(n) for n in connections[node])


@functools.cache
def search2(node: str, seen: tuple[bool, bool]) -> int:
    if node == "out":
        return 1 if seen == (True, True) else 0

    next_seen = (
        seen[0] or node == "dac",
        seen[1] or node == "fft",
    )

    return sum(search2(n, next_seen) for n in connections[node])


p1total = search("you")
p2total = search2("svr", (False, False))


print(f"{p1total = }")
print(f"{p2total = }")
