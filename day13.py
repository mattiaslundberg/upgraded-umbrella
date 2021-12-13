import sys

with open("./input/day13.txt") as f:
    raw = f.readlines()

    dots = {}
    folds = []

    for r in raw:
        if "," in r:
            dots[tuple(map(int, r.strip().split(",")))] = 1
        if r.startswith("fold along"):
            [d, v] = r.strip().split(" ")[2].split("=")
            folds.append((d, int(v)))


def do_fold(direction, location, dots):
    result = dots.copy()
    if direction == "x":
        for x in range(location, 1400):
            for y in range(1400):
                if (x, y) in dots:
                    new_x = location - (x - location)
                    del result[(x, y)]
                    result[(new_x, y)] = 1
    else:
        for x in range(1400):
            for y in range(location, 1400):
                if (x, y) in dots:
                    new_y = location - (y - location)
                    del result[(x, y)]
                    result[(x, new_y)] = 1
    return result


(direction, location) = folds[0]
next_dots = do_fold(direction, location, dots)
result = sum(next_dots.values())
print(f"Part 1: {result}")

final_dots = dots.copy()
for (direction, location) in folds:
    final_dots = do_fold(direction, location, final_dots)

max_x = 0
max_y = 0
for (x, y), v in final_dots.items():
    max_x = max(x, max_x)
    max_y = max(y, max_y)

print("#### Part 2 ####")
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if (x, y) in final_dots:
            sys.stdout.write("#")
        else:
            sys.stdout.write(" ")
    print()
print("####        ####")
