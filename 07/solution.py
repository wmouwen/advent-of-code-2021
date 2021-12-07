import math
import statistics
import sys

input = [int(point) for point in sys.stdin.readline().strip().split(',')]

# Part 1
median = int(statistics.median(input))
print(sum(abs(start - median) for start in input))

# Part 2
mean = statistics.mean(input)
candidates = range(math.floor(mean), math.ceil(mean) + 1)
print(min(sum((dist := abs(start - candidate)) * (dist + 1) // 2 for start in input) for candidate in candidates))
