with open("./input/day10.txt") as f:
    lines = []
    raw = f.readlines()
    for r in raw:
        lines.append(list(r.strip()))


def find_illegal(line, inside=[]):
    if len(line) <= 0:
        return False, reversed(inside)

    current = line[0]
    tail = line[1:]
    new_inside = inside.copy()

    if current in ["[", "{", "(", "<"]:
        new_inside.append(current)
    elif current == "]":
        inside_last = new_inside.pop()
        if inside_last != "[":
            return True, current
    elif current == "}":
        inside_last = new_inside.pop()
        if inside_last != "{":
            return True, current
    elif current == ")":
        inside_last = new_inside.pop()
        if inside_last != "(":
            return True, current
    elif current == ">":
        inside_last = new_inside.pop()
        if inside_last != "<":
            return True, current
    return find_illegal(tail, new_inside)


result1 = 0
result2 = []
for line in lines:
    incomplete, illegal = find_illegal(line)
    if incomplete:
        if illegal == ")":
            result1 += 3
        elif illegal == "]":
            result1 += 57
        elif illegal == "}":
            result1 += 1197
        elif illegal == ">":
            result1 += 25137
    else:
        res = 0
        for i in illegal:
            if i == "(":
                res *= 5
                res += 1
            elif i == "[":
                res *= 5
                res += 2
            elif i == "{":
                res *= 5
                res += 3
            elif i == "<":
                res *= 5
                res += 4
        result2.append(res)

result2.sort()

print(f"Part 1: {result1}")
print(f"Part 2: {result2[int(len(result2)/2)]}")
