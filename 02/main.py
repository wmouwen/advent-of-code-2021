import sys

horizontal_position = 0
aim = 0
depth = 0

for line in sys.stdin:
    [direction, steps] = line.strip().split(' ')
    steps = int(steps)

    if direction == 'forward':
        horizontal_position += steps
        depth += aim * steps

    elif direction == 'down':
        aim += steps

    elif direction == 'up':
        aim -= steps

print(aim * horizontal_position)
print(depth * horizontal_position)
