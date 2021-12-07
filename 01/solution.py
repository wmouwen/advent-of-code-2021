import sys

values = []

for line in sys.stdin:
    values.append(int(line.strip()))

increments_single = 0
increments_moving_average = 0

for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        increments_single += 1

    if i >= 3 and values[i] > values[i - 3]:
        increments_moving_average += 1

print(increments_single)
print(increments_moving_average)
