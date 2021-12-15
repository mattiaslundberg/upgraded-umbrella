import sys
from copy import deepcopy
from functools import lru_cache
from queue import PriorityQueue

sys.setrecursionlimit(5000)

with open("./input/day15.txt") as f:
    raw = f.readlines()
    risks = []
    for r in raw:
        risks.append(list(map(int, list(r.strip()))))


def inc(n):
    if n >= 9: return 1
    else: return n + 1


def increase_row(locs):
    return [inc(n) for n in locs]


tmp = deepcopy(risks)
previous = tmp
for i in range(4):
    nn = [increase_row(l) for l in previous]
    previous = nn
    tmp += nn

risks2 = []
for l in tmp:
    res = l
    previous = l
    for _ in range(4):
        nn = increase_row(previous)
        previous = nn
        res += nn
    risks2.append(res)



def find_path(location, goal, r):
    (gx, gy) = goal
    distances = {}

    to_visit = PriorityQueue()
    to_visit.put((0, location))


    for x in range(len(r)):
        for y in range(len(r[0])):
            distances[(x, y)] = 9999999999

    distances[location] = 0

    while not to_visit.empty():
        (dist, current) = to_visit.get()
        (x, y) = current

        for (nx, ny) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if nx < 0 or ny < 0 or nx > gx or ny > gy:
                continue
            alt = distances[current] + r[nx][ny]
            if alt < distances[(nx, ny)]:
                distances[(nx, ny)] = alt
                to_visit.put((alt, (nx, ny)))

    return distances[goal]

location = (0, 0)
goal = (len(risks) - 1, len(risks[0]) - 1)
print(f"Part 1: {find_path(location, goal, risks)}")
goal = (len(risks2) - 1, len(risks2[0]) - 1)
print(f"Part 2: {find_path(location, goal, risks2)}")
