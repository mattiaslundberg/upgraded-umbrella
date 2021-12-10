with open("./input/day10.txt") as f:
    lines = []
    raw = f.readlines()
    for r in raw:
        lines.append(list(r.strip()))


def find_illegal(line, inside=[]):
    if len(line) <= 0:
        return None

    current = line[0]
    tail = line[1:]
    new_inside = inside.copy()

    if current in ["[", "{", "(", "<"]:
        new_inside.append(current)
    elif current == "]":
        inside_last = new_inside.pop()
        if inside_last != "[":
            return current
    elif current == "}":
        inside_last = new_inside.pop()
        if inside_last != "{":
            return current
    elif current == ")":
        inside_last = new_inside.pop()
        if inside_last != "(":
            return current
    elif current == ">":
        inside_last = new_inside.pop()
        if inside_last != "<":
            return current
    return find_illegal(tail, new_inside)


result = 0
for line in lines:
    illegal = find_illegal(line)
    if illegal == ")":
        result += 3
    if illegal == "]":
        result += 57
    if illegal == "}":
        result += 1197
    if illegal == ">":
        result += 25137

print(f"Part 1: {result}")

correct_lines = []
for line in lines:
    illegal = find_illegal(line)
    if not illegal:
        correct_lines.append(line)
