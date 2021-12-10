with open("./input/day10.txt") as f:
    lines = []
    raw = f.readlines()
    for r in raw:
        lines.append(list(r.strip()))


matching = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"

}


def find_illegal(line, inside=[]):
    if len(line) <= 0:
        return False, reversed(inside)

    current = line[0]
    tail = line[1:]
    new_inside = inside.copy()

    if current in ["[", "{", "(", "<"]:
        new_inside.append(current)
    else:
        inside_last = new_inside.pop()
        if inside_last != matching[current]:
            return True, current
    return find_illegal(tail, new_inside)

vals1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

vals2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

result1 = 0
result2 = []
for line in lines:
    incomplete, illegal = find_illegal(line)
    if incomplete:
        result1 += vals1[illegal]
    else:
        res = 0
        for i in illegal:
            res *= 5
            res += vals2[i]
        result2.append(res)

result2.sort()

print(f"Part 1: {result1}")
print(f"Part 2: {result2[int(len(result2)/2)]}")
