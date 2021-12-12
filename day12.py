from collections import defaultdict, Counter

with open("./input/day12.txt") as f:
    raw = f.readlines()
    edges = []
    for r in raw:
        edges.append(r.strip().split("-"))

paths = defaultdict(list)

for a, b in edges:
    paths[a].append(b)
    paths[b].append(a)


def find_path(location, visited_small, max_small_visits):
    if location == "end":
        return 1
    if visited_small["start"] >= 1 and location == "start":
        return 0
    if visited_small[location] >= max_small_visits:
        return 0

    if location.islower():
        visited_small = visited_small.copy()
        visited_small[location] += 1

        c = Counter(visited_small.values())
        if visited_small[location] >= max_small_visits and c[2] >= 2:
            return 0

    result = 0
    nexts = paths[location]
    for n in nexts:
        result += find_path(n, visited_small, max_small_visits)
    return result


result = find_path("start", defaultdict(int), 1)
print(f"Part 1: {result}")

result = find_path("start", defaultdict(int), 2)
print(f"Part 2: {result}")
