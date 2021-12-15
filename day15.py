import sys
from functools import lru_cache

sys.setrecursionlimit(5000)


with open("./input/day15.txt") as f:
    raw = f.readlines()
    risks = []
    for r in raw:
        risks.append(list(map(int, list(r.strip()))))


@lru_cache
def find_path(location, goal):
    (x, y) = location
    (gx, gy) = goal
    risk = risks[x][y]

    if x == gx and y == gy:
        return risk

    min_path = 9999999
    if x < len(risks) - 1:
        min_path = min(min_path, find_path((x + 1, y), goal))
    if y < len(risks[0]) - 1:
        min_path = min(min_path, find_path((x, y + 1), goal))
    if x == 0 and y == 0:
        return min_path
    return min_path + risk


location = (0, 0)
goal = (len(risks) - 1, len(risks[0]) - 1)


print(f"Part 1: {find_path(location, goal)}")


def inc(n):
    if n >= 9:
        return 1
    else:
        return n + 1


def increase(locs):
    r = []
    for l in locs:
        ri = []
        for c in l:
            ri.append(inc(c))
        r.append(ri)
    return r


def increase_row(locs):
    return [inc(n) for n in locs]


risks2 = risks.copy()
previous = risks2
for i in range(4):
    nn = increase(previous)
    previous = nn
    risks2 += nn

risks3 = []
for l in risks2:
    res = l
    previous = l
    for _ in range(4):
        nn = increase_row(previous)
        previous = nn
        res += nn
    risks3.append(res)
risks2 = risks3


@lru_cache
def find_path2(location, goal):
    (x, y) = location
    (gx, gy) = goal
    risk = risks2[x][y]

    if x == gx and y == gy:
        return risk

    min_path = 9999999999999
    if x < len(risks2) - 1:
        min_path = min(min_path, find_path2((x + 1, y), goal))
    if y < len(risks2[0]) - 1:
        min_path = min(min_path, find_path2((x, y + 1), goal))
    if x == 0 and y == 0:
        return min_path
    return min_path + risk


goal = (len(risks2) - 1, len(risks2[0]) - 1)
print(f"Part 2: {find_path2(location, goal)}")
