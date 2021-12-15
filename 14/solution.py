import re
import sys


def tick(old_pairs: dict, replacements: dict) -> dict:
    new_pairs = {}

    for pair in old_pairs:
        for replacement in replacements[pair]:
            if replacement not in new_pairs:
                new_pairs[replacement] = 0

            new_pairs[replacement] += old_pairs[pair]

    return new_pairs


def count_elements(pairs: dict, last_element: str) -> dict:
    elements = {last_element: 1}

    for pair in pairs:
        element = pair[0]

        if element not in elements:
            elements[element] = 0

        elements[element] += pairs[pair]

    return elements


pairs = {}
last_element = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        break

    for i in range(len(line) - 1):
        pair = line[i:i + 2]

        if pair not in pairs:
            pairs[pair] = 0

        pairs[pair] += 1

    last_element = line[-1]

replacements = {}

for line in sys.stdin:
    (pair, insertion) = re.match(r'^(\w+) -> (\w)$', line.strip()).groups()
    replacements[pair] = [pair[0] + insertion, insertion + pair[1]]

for i in range(1, 41):
    pairs = tick(pairs, replacements)

    if i in [10, 40]:
        elements = count_elements(pairs, last_element)
        print(max(elements.values()) - min(elements.values()))
