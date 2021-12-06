import sys

def simulate(fish, days):
    for i in range(days):
        fish = fish[1:] + fish[:1]
        fish[6] += fish[8]

    return fish


input = list(map(int, sys.stdin.readline().strip().split(',')))
buckets = {bucket: input.count(bucket) for bucket in set(input)}

fish = [0] * 9
for day, amount in buckets.items():
    fish[day] = amount

print(sum(simulate(fish, 80)))
print(sum(simulate(fish, 256)))
