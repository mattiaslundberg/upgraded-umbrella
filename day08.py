from collections import Counter

with open("./input/day08.txt") as f:
    raw = f.readlines()

displays = []
for r in raw:
    in_raw, out_raw = r.split(" | ")

    displays.append((in_raw.strip().split(" "), out_raw.strip().split(" ")))

print(displays)


result = 0

for _, out_vals in displays:
    lens = list(map(len, out_vals))
    c = Counter(lens)
    result += c.get(2, 0) + c.get(4, 0) + c.get(3, 0) + c.get(7, 0)

print(f"Part 1 {result}")
