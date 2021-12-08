import sys

occurences = 0
total = 0

for line in sys.stdin:
    digits, code = ([''.join(sorted(digit)) for digit in parts.split()] for parts in line.split('|'))

    digit_map = {
        1: next(d for d in digits if len(d) == 2),
        4: next(d for d in digits if len(d) == 4),
        7: next(d for d in digits if len(d) == 3),
        8: next(d for d in digits if len(d) == 7)
    }

    occurences += len([digit for digit in code if digit in digit_map.values()])

    digit_map.update({
        3: next(d for d in digits if len(d) == 5 and all(char in d for char in digit_map[1])),
        6: next(d for d in digits if len(d) == 6 and any(char not in d for char in digit_map[1])),
        9: next(d for d in digits if len(d) == 6 and all(char in d for char in digit_map[4]))
    })

    digit_map.update({
        5: next(d for d in digits if len(d) == 5 and d not in digit_map.values() and sum([c in d for c in digit_map[4]]) == 3),
    })

    digit_map.update({
        0: next(d for d in digits if len(d) == 6 and d not in digit_map.values()),
        2: next(d for d in digits if len(d) == 5 and d not in digit_map.values())
    })

    total += int(''.join(next(str(key) for key, value in digit_map.items() if value == digit) for digit in code))

print(occurences)
print(total)
