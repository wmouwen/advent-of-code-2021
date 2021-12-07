import sys


def simulate(fish, days):
    for day in range(days):
        fish = fish[1:] + fish[:1]
        fish[6] += fish[8]

    return sum(fish)


fish = [0] * 9
for f in list(map(int, sys.stdin.readline().strip().split(','))):
    fish[f] += 1

print(simulate(fish, 80))
print(simulate(fish, 256))
