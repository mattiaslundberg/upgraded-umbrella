from collections import defaultdict

with open("./input/day12.txt") as f:
    raw = f.readlines()
    edges = []
    for r in raw:
        edges.append(r.strip().split("-"))

paths = defaultdict(list)

for a, b in edges:
    paths[a].append(b)
    paths[b].append(a)


def find_path(location, visited_small):
    if location == "end":
        return 1
    if location in visited_small:
        return 0

    nexts = paths[location]
    if location.islower():
        visited_small = visited_small + [location]

    result = 0
    for n in nexts:
        result += find_path(n, visited_small)
    return result


result = find_path("start", [])
print(f"Part 1: {result}")
