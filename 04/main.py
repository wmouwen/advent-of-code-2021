import sys


class Board:
    def __init__(self):
        self.numbers = []
        self.called = []

    def add_row(self, values) -> None:
        self.numbers.append(values)
        self.called.append([False] * len(values))

    def mark(self, value) -> None:
        for y in range(len(self.numbers)):
            for x in range(len(self.numbers[y])):
                if self.numbers[y][x] == value:
                    self.called[y][x] = True
                    return

    def has_bingo(self) -> bool:
        # Check rows
        for row in self.called:
            bingo = True

            for field in row:
                bingo = bingo & field

            if bingo:
                return True

        # Check columns
        for x in range(len(self.called[0])):
            bingo = True

            for y in range(len(self.called)):
                bingo = bingo & self.called[y][x]

            if bingo:
                return True

        return False

    def sum_of_unmarked_numbers(self) -> int:
        unmarked_sum = 0

        for y, row in enumerate(self.numbers):
            for x, field in enumerate(row):
                if not self.called[y][x]:
                    unmarked_sum += field

        return unmarked_sum


# Load callouts
callouts = list(map(int, sys.stdin.readline().strip().split(',')))

# Init boards
boards = []
for line in sys.stdin:
    line = line.strip()

    if not line:
        boards.append(Board())
        continue

    boards[-1].add_row(list(map(int, line.split())))

# Filter out empty boards due to uncaught blank lines
boards = list(filter(lambda board: len(board.numbers), boards))

# Play Bingo
first_win_score = None
last_win_score = None

for callout in callouts:
    for board in boards:
        board.mark(callout)

        if board.has_bingo():
            last_win_score = board.sum_of_unmarked_numbers() * callout
            if first_win_score is None:
                first_win_score = last_win_score

    boards = list(filter(lambda board: not board.has_bingo(), boards))

    if not len(boards):
        break

print(first_win_score)
print(last_win_score)
