import math
import sys


def find_low_points(height_map: list) -> list:
    low_points = []

    for y, row in enumerate(height_map):
        for x, field in enumerate(row):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < len(row) and 0 <= y + dy < len(height_map):
                    if height_map[y + dy][x + dx] <= field:
                        break
            else:
                low_points.append((x, y))

    return low_points


def find_basin(height_map: list, low_point: tuple) -> list:
    queue = [low_point]
    basin = []

    while len(queue):
        (x, y) = queue.pop()

        if height_map[y][x] == 9:
            continue

        basin.append((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(height_map[y]) and 0 <= y + dy < len(height_map) \
                    and not (x + dx, y + dy) in basin and not (x + dx, y + dy) in queue:
                queue.append((x + dx, y + dy))

    return basin


height_map = [[int(field) for field in row.strip()] for row in sys.stdin]
low_points = find_low_points(height_map)

print(sum(height_map[y][x] + 1 for (x, y) in low_points))

basin_sizes = [len(find_basin(height_map, low_point)) for low_point in low_points]
basin_sizes.sort(reverse=True)

print(math.prod(basin_sizes[:3]))
