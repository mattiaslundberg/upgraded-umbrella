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

def get_dangerous(diagonals):
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
        elif diagonals and abs(x1 - x2) == abs(y1 - y2):
            if x1 < x2 and y1 < y2:
                for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                    visits[(x, y)] += 1
            elif x1 > x2 and y1 > y2:
                for x, y in zip(range(x2, x1 + 1), range(y2, y1 + 1)):
                    visits[(x, y)] += 1
            elif x1 < x2 and y1 > y2:
                for x, y in zip(range(x1, x2 + 1), reversed(range(y2, y1 + 1))):
                    visits[(x, y)] += 1
            else:
                for x, y in zip(reversed(range(x2, x1 + 1)), range(y1, y2 + 1)):
                    visits[(x, y)] += 1

    dangerous = 0
    for count in visits.values():
        if count > 1:
            dangerous += 1
    return dangerous

dangerous = get_dangerous(False)
print(f"Part 1: {dangerous}")

dangerous = get_dangerous(True)
print(f"Part 2: {dangerous}")
