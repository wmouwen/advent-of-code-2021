import sys


class Point:
    def __init__(self, str):
        coordinates = str.split(',')
        self.x = int(coordinates[0])
        self.y = int(coordinates[1])


def amount_of_crossings(lines) -> int:
    max_y, max_x = 0, 0

    for [start, end] in lines:
        max_y = max(max_y, start.y, end.y)
        max_x = max(max_x, start.x, end.x)

    plane = []
    for y in range(max_y + 1):
        plane.append([0] * (max_x + 1))

    for [start, end] in lines:
        # Non-orthogonal lines
        if start.x != end.x and start.y != end.y:
            direction = 1 if end.x >= start.x else -1
            for offset in range(end.y - start.y + 1):
                plane[start.y + offset][start.x + offset * direction] += 1

        else:
            # Orthogonal lines
            for y in range(start.y, end.y + 1):
                for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
                    plane[y][x] += 1

    # Count crossings
    crossings = 0
    for row in plane:
        for field in row:
            crossings += 1 if field > 1 else 0

    return crossings


# Read input
lines = []
for input_line in sys.stdin:
    input_line = input_line.strip().split(' -> ')
    start = Point(input_line[0])
    end = Point(input_line[1])

    if end.y < start.y:
        tmp = end
        end = start
        start = tmp

    lines.append([start, end])


orthogonalLines = list(filter(lambda line: line[0].x == line[1].x or line[0].y == line[1].y,lines))
print(amount_of_crossings(orthogonalLines))
print(amount_of_crossings(lines))
