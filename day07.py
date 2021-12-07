with open("./input/day07.txt") as f:
    positions = list(map(int, f.read().split(',')))

min_fuel = 999999

for i in range(1000):
    fuel = 0
    for position in positions:
        fuel += abs(position - i)

    min_fuel = min(fuel, min_fuel)

print(f"Part 1 {min_fuel}")
