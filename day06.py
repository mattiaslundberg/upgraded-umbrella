from collections import Counter

with open("./input/day06.txt") as f:
    initial = map(int, f.read().split(","))


def do_move(state):
    return {
        0: state.get(1, 0),
        1: state.get(2, 0),
        2: state.get(3, 0),
        3: state.get(4, 0),
        4: state.get(5, 0),
        5: state.get(6, 0),
        6: state.get(7, 0) + state.get(0, 0),
        7: state.get(8, 0),
        8: state.get(0, 0),
    }


state = dict(Counter(initial))
for i in range(256):
    state = do_move(state)

    if i == 79:
        result = sum(state.values())
        print(f"Part 1: {result}")

result = sum(state.values())
print(f"Part 2: {result}")
