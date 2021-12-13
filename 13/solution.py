import re
import sys


def fold(unfolded: set, axis: str, value: int) -> set:
    folded = set()

    for (x, y) in unfolded:
        if axis == 'x' and x > value:
            x = value - (x - value)
        if axis == 'y' and y > value:
            y = value - (y - value)

        folded.add((x, y))

    return folded


points = set()

for line in sys.stdin:
    line = line.strip()
    if not line:
        break

    points.add(tuple(int(coordinate) for coordinate in line.split(',')))

points_after_first_fold = None

for line in sys.stdin:
    (axis, value) = re.match(r'^fold along ([xy])=(\d+)$', line.strip()).groups()

    points = fold(points, axis, int(value))

    if points_after_first_fold is None:
        points_after_first_fold = len(points)

print(points_after_first_fold)

for y in range(max(y for (x, y) in points) + 1):
    line = ''
    for x in range(max(x for (x, y) in points) + 1):
        line += '#' if (x, y) in points else '.'
    print(line)
