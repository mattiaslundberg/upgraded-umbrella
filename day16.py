examples = {
    "D2FE28": 2021,
    "38006F45291200": None,
    "EE00D40C823060": None,
    "8A004A801A8002F478": None,
    "620080001611562C8802118E34": None,
    "C0015000016115A2E0802F182340": None,
    "A0016C880162017C3686B18A3D4780": None,
}

with open("./input/day16.txt") as f:
    real = f.readline().strip()


def parse_package(remaining, max_count):
    if len(remaining) < 8 or max_count <= 0:
        return 0, 0, []
    packet_version = int("".join(remaining[:3]), 2)
    type_id = int("".join(remaining[3:6]), 2)

    result = None
    if type_id == 4:
        remaining = remaining[6:]
        pv = 0
        value = []
        while True:
            block = remaining[:5]
            remaining = remaining[5:]
            value += block[1:]
            if block[0] == "0":
                _, pv, outside = parse_package(remaining, max_count - 1)
                break
        result = int("".join(value), 2)
    else:
        remaining = remaining[6:]
        len_type_id = int("".join(remaining[:1]))
        remaining = remaining[1:]
        if len_type_id == 0:
            length = int("".join(remaining[:15]), 2)
            inside = remaining[15:]
            _, pv, outside = parse_package(inside, float("inf"))
            _, pv2, _ = parse_package(outside, float("inf"))
            pv += pv2
        elif len_type_id == 1:
            length = int("".join(remaining[:11]), 2)
            inside = remaining[11:]
            _, pv, outside = parse_package(inside, length)
            _, pv2, _ = parse_package(outside, float("inf"))
            pv += pv2
        else:
            print("Unknown package!")
    return result, packet_version + pv, []


for example, expected in examples.items():
    ee = ""
    for x in list(example):
        e = bin(int(x, 16))[2:].zfill(4)
        ee += e
    e = list(ee)

    result, version_sum, _ = parse_package(e, float("inf"))

    print(example, result, version_sum, result == expected)


ee = ""
for x in list(real):
    e = bin(int(x, 16))[2:].zfill(4)
    ee += e
e = list(ee)

result, version_sum, _ = parse_package(e, float("inf"))
print(f"Part 1: {version_sum}")
