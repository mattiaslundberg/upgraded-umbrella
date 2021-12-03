
with open("./input/day03.txt") as f:
    lines = list(map(lambda l: l.strip(), f.readlines()))

zeros = [0] * len(lines[0])
ones = [0] * len(lines[0])

for line in lines:
    items = list(map(int, list(line)))

    for i, v in enumerate(items):
        if v == 0:
            zeros[i] += 1
        if v == 1:
            ones[i] += 1



gamma = []
epsilon = []
for zero, one in zip(zeros, ones):
    if zero < one:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

epsilon = int("".join(map(str, epsilon)), 2)
gamma = int("".join(map(str, gamma)), 2)

print(f"Part 1: {gamma * epsilon}")


def get_by_common(lines, most, loc):
    ones_count = 0
    zeros_count = 0

    for line in lines:
        value = int(line[loc])
        if value == 0:
            zeros_count += 1
        else:
            ones_count += 1

    if ones_count > zeros_count:
        val = 1 if most else 0
        to_count = list(filter(lambda l: int(l[loc]) == val, lines))
    elif ones_count == zeros_count:
        val = 1 if most else 0
        to_count = list(filter(lambda l: int(l[loc]) == val, lines))
    else:
        val = 0 if most else 1
        to_count = list(filter(lambda l: int(l[loc]) == val, lines))


    if len(to_count) == 1:
        return int("".join(map(str, to_count[0])), 2)

    return get_by_common(to_count, most, loc + 1)

lines = [list(map(int, l)) for l in lines]
ogr = get_by_common(lines, True, 0)
csr = get_by_common(lines, False, 0)

print(f"Part 2: {ogr * csr}")
