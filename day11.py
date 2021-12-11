with open("./input/day11.txt") as f:
    raw = f.readlines()
    lines = []
    for r in raw:
        lines.append(list(map(int, list(r.strip()))))


def increase_one(lines):
    for x in range(10):
        for y in range(10):
            lines[x][y] += 1
    return lines


def do_flashes(lines):
    flashed = []
    found_last = 1
    while found_last:
        found_last = 0
        for x in range(10):
            for y in range(10):
                if (x, y) not in flashed and lines[x][y] > 9:
                    found_last += 1
                    flashed.append((x, y))
                    if x > 0:
                        lines[x - 1][y] += 1
                        if y < 9:
                            lines[x - 1][y + 1] += 1
                        if y > 0:
                            lines[x - 1][y - 1] += 1
                    if x < 9:
                        lines[x + 1][y] += 1
                        if y < 9:
                            lines[x + 1][y + 1] += 1
                        if y > 0:
                            lines[x + 1][y - 1] += 1
                    if y < 9:
                        lines[x][y + 1] += 1
                    if y > 0:
                        lines[x][y - 1] += 1

    flash_count = 0
    for x in range(10):
        for y in range(10):
            if lines[x][y] > 9:
                flash_count += 1
                lines[x][y] = 0

    return flash_count, lines


flash_count = 0
for i in range(1000):
    lines = increase_one(lines)
    flashes, lines = do_flashes(lines)
    flash_count += flashes
    if i == 99:
        print(f"Part 1 {flash_count}")
    if flashes == 100:
        print(f"Part 2 {i + 1}")
        break
