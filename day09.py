with open("./input/day09.txt") as f:
    raw = f.readlines()

    lines = []
    for l in raw:
        r = list(map(int, list(l.strip())))
        lines.append(r)


def low_points(depths):
    res = []
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
                res.append(curr)
    return res


low = low_points(lines)

print(f"Part 1: {len(low) + sum(low)}")
