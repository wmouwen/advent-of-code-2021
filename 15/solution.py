import math
import sys


def calc_lowest_costs(cost_map: list, start: tuple) -> list:
    (x, y) = start

    lowest_cost_map = [[math.inf] * len(row) for row in cost_map]
    lowest_cost_map[y][x] = 0

    queue = {start}
    directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}

    while queue:
        (x, y) = queue.pop()

        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)

            if not (0 <= ny < len(lowest_cost_map)):
                continue
            if not (0 <= nx < len(lowest_cost_map[ny])):
                continue

            new_cost = lowest_cost_map[y][x] + cost_map[ny][nx]

            if new_cost < lowest_cost_map[ny][nx]:
                lowest_cost_map[ny][nx] = new_cost
                queue.add((nx, ny))

    return lowest_cost_map


def tile(input: list, vx: int, vy: int) -> list:
    (x_max, y_max) = (len(input[0]), len(input))

    output = []
    for x in range((y_max * vy)):
        output.append([0] * (x_max * vx))

    for y in range(len(output)):
        for x in range(len(output[y])):
            output[y][x] = ((input[y % y_max][x % x_max] + (y // y_max) + (x // x_max) - 1) % 9) + 1

    return output


# Read input
map = []
for line in sys.stdin:
    map.append([int(field) for field in line.strip()])

# Part 1
lowest_cost_map = calc_lowest_costs(map, (0, 0))
print(lowest_cost_map[-1][-1])

# Tile map vertically
map = tile(map, 5, 5)
lowest_cost_map = calc_lowest_costs(map, (0, 0))
print(lowest_cost_map[-1][-1])
