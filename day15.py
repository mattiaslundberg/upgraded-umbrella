from functools import lru_cache

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


print(find_path(location, goal))
