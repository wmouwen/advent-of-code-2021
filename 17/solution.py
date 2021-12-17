import re
import sys


def find_vy(y_min, y_max, initial_vx, x_min, x_max) -> int:
    for candidate_vy in range(max(x_max, abs(y_max))):
        vx = initial_vx
        vy = candidate_vy
        (x, y) = (0, 0)

        while y_min <= y and x <= x_max:
            # Broken
            x += vx
            vx -= 1

            y += vy
            vy -= 1

            if y_min <= y <= y_max:
                return candidate_vy


input = re.match(r'^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$', sys.stdin.read()).groups()
(x_min, x_max, y_min, y_max) = (int(group) for group in input)

print(x_min, x_max, y_min, y_max)

vx = 0
x = 0
while not (x_min <= x <= x_max):
    vx += 1
    x += vx

vy = find_vy(y_min, y_max, vx, x_min, x_max)
print(vx, vy)
print((vy * (vy + 1)) // 2)
