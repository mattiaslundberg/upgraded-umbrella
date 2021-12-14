from collections import Counter

with open("./input/day14.txt") as f:
    initial = list(f.readline().strip())

    mappings = {}
    raw = f.readlines()
    for r in raw:
        if "->" in r:
            [start, to] = r.strip().split(" -> ")
            mappings[start] = to


def do_map(initial):
    result = []
    result.append(initial[0])
    for i in range(1, len(initial)):
        insert = mappings.get(f"{initial[i-1]}{initial[i]}")
        if insert:
            result += [insert, initial[i]]
        else:
            result += [initial[i]]
    return result


state = initial
for _ in range(10):
    state = do_map(state)


counter = Counter(state)
values = sorted(counter.values())
print(f"Part 1: {values[-1] - values[0]}")
