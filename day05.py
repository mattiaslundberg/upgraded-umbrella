from collections import defaultdict
with open("./input/day05.txt") as f:
    raw = f.readlines()

    lines = []
    for line in raw:
        line = line.strip()
        [one, two] = line.split(" -> ")

        [x1, y1] = map(int, one.split(","))
        [x2, y2] = map(int, two.split(","))
        lines.append((x1, y1, x2, y2))

visits = defaultdict(int)
for x1, y1, x2, y2 in lines:
    if x1 == x2:
        [yl, yh] = sorted([y1, y2])
        for y in range(yl, yh + 1):
            visits[(x1, y)] += 1
    elif y1 == y2:
        [xl, xh] = sorted([x1, x2])
        for x in range(xl, xh + 1):
            visits[(x, y1)] += 1

dangerous = 0
for location, count in visits.items():
    if count > 1:
        dangerous += 1

print(f"Part 1: {dangerous}")
