from collections import Counter

with open("./input/day08.txt") as f:
    raw = f.readlines()

displays = []
for r in raw:
    in_raw, out_raw = r.split(" | ")

    displays.append((in_raw.strip().split(" "), out_raw.strip().split(" ")))

result = 0

for _, out_vals in displays:
    lens = list(map(len, out_vals))
    c = Counter(lens)
    result += c.get(2, 0) + c.get(4, 0) + c.get(3, 0) + c.get(7, 0)

print(f"Part 1 {result}")


result = 0
for in_vals, out_vals in displays:
    in_vals = list(map(set, in_vals))
    vals = dict()
    while len(in_vals):
        current = in_vals.pop()
        if len(current) == 2: # 1
            vals[1] = current
        elif len(current) == 4: # 4
            vals[4] = current
        elif len(current) == 3: # 7
            vals[7] = current
        elif len(current) == 7: # 8
            vals[8] = current
        elif len(vals) < 4:
            in_vals.insert(0, current)
        elif len(current) == 6: # 0 or 6 or 9
            if vals[4] <= current:
                vals[9] = current
            elif vals[1] <= current:
                vals[0] = current
            else:
                vals[6] = current
        elif len(current) == 5: # 2, 3, 5
            if vals[1] <= current:
                vals[3] = current
            elif len(current - vals[4]) == 3:
                vals[2] = current
            else:
                vals[5] = current


    full_result = ""
    for v in out_vals:
        vv = set(v)
        for k, x in vals.items():
            if vv == x:
                full_result += str(k)
    result += int(full_result)


print(f"Part 2 {result}")
