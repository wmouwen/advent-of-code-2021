import math
import sys

values = []

for line in sys.stdin:
    line = line.strip()
    values.append(line)


def find_most_common(values, position):
    stat = 0

    for value in values:
        stat += 1 if value[position] == '1' else -1

    return '1' if stat >= 0 else '0'


# Part 1
gammaRate = ''
for position in range(0, len(values[0])):
    gammaRate += find_most_common(values, position)

gammaRate = int(gammaRate, 2)
epsilonRate = int(math.pow(2, len(values[0])) - 1) - gammaRate

print(gammaRate * epsilonRate)

# Part 2
candidates = values.copy()
for position in range(0, len(values[0])):
    target = find_most_common(candidates, position)
    candidates = list(filter(lambda value: value[position] == target, candidates))
    if len(candidates) <= 1:
        break

oxygenGeneratorRating = int(candidates[0], 2)

candidates = values.copy()
for position in range(0, len(values[0])):
    target = find_most_common(candidates, position)
    candidates = list(filter(lambda value: value[position] != target, candidates))
    if len(candidates) <= 1:
        break

co2ScrubberRating = int(candidates[0], 2)

print(oxygenGeneratorRating * co2ScrubberRating)
