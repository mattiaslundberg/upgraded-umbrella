from collections import Counter, defaultdict

with open("./input/day14.txt") as f:
    initial = list(f.readline().strip())

    mappings = {}
    raw = f.readlines()
    for r in raw:
        if "->" in r:
            [start, to] = r.strip().split(" -> ")
            [s1, s2] = list(start)
            mappings[(s1, s2)] = to


def do_count(num, initial):
    counts = Counter(initial)
    c = Counter(zip(initial, initial[1:]))
    for _ in range(num):
        next_c = Counter()
        for (first, second), count in c.items():
            new = mappings[(first, second)]
            next_c[(first, new)] += count
            next_c[(new, second)] += count
            counts[new] += count
        c = next_c
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


print(f"Part 1: {do_count(10, initial)}")
print(f"Part 1: {do_count(40, initial)}")
