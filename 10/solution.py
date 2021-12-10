import sys

bracket_counterparts = {')': '(', ']': '[', '}': '{', '>': '<'}
error_values = {')': 3, ']': 57, '}': 1197, '>': 25137}
contest_values = {'(': 1, '[': 2, '{': 3, '<': 4}

error_score = 0
contest_scores = []

for line in sys.stdin:
    stack = []

    for current in line.strip():
        if current in "<{[(":
            stack.append(current)
            continue

        if not stack or bracket_counterparts[current] != stack.pop():
            error_score += error_values[current]
            break

    else:
        contest_score = 0
        while stack:
            contest_score = contest_score * 5 + contest_values[stack.pop()]
        contest_scores.append(contest_score)

print(error_score)

contest_scores.sort()
print(contest_scores[len(contest_scores) // 2])
