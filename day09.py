with open("./input/day09.txt") as f:
    raw = f.readlines()

    lines = []
    for l in raw:
        r = list(map(int, list(l.strip())))
        lines.append(r)


def low_points(depths):
    res = {}
    for x in range(len(depths)):
        for y in range(len(depths[0])):
            curr = depths[x][y]
            if x < len(depths) - 1 and curr >= depths[x + 1][y]:
                pass
            elif x > 0 and curr >= depths[x - 1][y]:
                pass
            elif y < len(depths[0]) - 1 and curr >= depths[x][y + 1]:
                pass
            elif y > 0 and curr >= depths[x][y - 1]:
                pass
            else:
                res[(x, y)] = curr
    return res


lows = low_points(lines)

print(f"Part 1: {len(lows.values()) + sum(lows.values())}")

def find_basin(x, y, excluded):
    if (x, y) in excluded:
        return None, 0
    if x < 0 or y < 0:
        return None, 0
    if x == len(lines) or y == len(lines[0]):
        return None, 0
    if lines[x][y] == 9:
        return None, 0

    size = 1
    excluded += [(x, y)]
    for xc, yc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        e, s = find_basin(xc, yc, excluded)
        size += s
        if s > 0 and (xc, yc) not in excluded:
            excluded += e

    return excluded, size



def find_basins(lows):
    res = []
    for xs, ys in lows.keys():
        r, basin = find_basin(xs, ys, [])
        res.append(basin)
    res = sorted(res, reverse=True)
    return res[:3]


[a, b, c] = find_basins(lows)

print(f"Part 2: {a * b * c}")
