import re
import sys


def reaches_target(x_min, x_max, y_min, y_max, vx, vy) -> bool:
    (x, y) = (0, 0)

    while x <= x_max and y_min <= y:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True

        (x, y) = (x + vx, y + vy)
        (vx, vy) = (max(0, vx - 1), vy - 1)

    return False


input = re.match(r'^target area: x=(\d+)..(\d+), y=(-\d+)..(-\d+)$', sys.stdin.read()).groups()
(x_min, x_max, y_min, y_max) = (int(group) for group in input)

possible_velocities = 0
max_height = 0

for vx in range(x_max + 1):
    for vy in range(y_min, -1 * y_min):
        if reaches_target(x_min, x_max, y_min, y_max, vx, vy):
            possible_velocities += 1
            max_height = max(max_height, (vy * (vy + 1)) // 2 if vy >= 0 else 0)

print(max_height)
print(possible_velocities)
