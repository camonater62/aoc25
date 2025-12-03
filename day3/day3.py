import sys


def largest_subsequence_digits(nums: list[int], N: int):
    M = len(nums)
    drop = M - N
    stack: list[int] = []

    for x in nums:
        while stack and drop > 0 and x > stack[-1]:
            stack.pop()
            drop -= 1
        stack.append(x)

    return stack[:N]


def largest_subsequence(nums: list[int], N: int):
    digits = largest_subsequence_digits(nums, N)
    return int("".join(map(str, digits)))


p1total = 0
p2total = 0

for bank in sys.stdin.readlines():
    bank = bank.strip()
    nums = [int(x) for x in bank]

    p1total += int(largest_subsequence(nums, 2))
    p2total += int(largest_subsequence(nums, 12))

print(f"{p1total = }")
print(f"{p2total = }")
