import sys


class Board:
    def __init__(self):
        self.numbers = []
        self.called = []

    def add_row(self, values) -> None:
        self.numbers.append(values)
        self.called.append([False] * len(values))

    def mark(self, value) -> None:
        for y in range(0, len(self.numbers)):
            for x in range(0, len(self.numbers[y])):
                if self.numbers[y][x] == value:
                    self.called[y][x] = True
                    return

    def has_bingo(self) -> bool:
        # Check rows
        for y in range(0, len(self.called)):
            bingo = True

            for x in range(0, len(self.called[y])):
                bingo = bingo & self.called[y][x]

            if bingo:
                return True

        # Check columns
        for x in range(0, len(self.called[0])):
            bingo = True

            for y in range(0, len(self.called)):
                bingo = bingo & self.called[y][x]

            if bingo:
                return True

        return False

    def sum_of_unmarked_numbers(self) -> int:
        unmarked_sum = 0

        for y in range(0, len(self.numbers)):
            for x in range(0, len(self.numbers[y])):
                if not self.called[y][x]:
                    unmarked_sum += self.numbers[y][x]

        return unmarked_sum


# Load callouts
callouts = list(map(int, sys.stdin.readline().strip().split(',')))

# Init boards
boards = []
for line in sys.stdin:
    line = line.strip().replace('  ', ' ')

    if not line:
        boards.append(Board())
        continue

    boards[len(boards) - 1].add_row(list(map(int, line.split(' '))))

# Filter out empty boards due to uncaught blank lines
boards = list(filter(lambda board: len(board.numbers), boards))

# Play Bingo
first_win_score = None
last_win_score = None

for callout in callouts:
    for board in boards:
        board.mark(callout)

        if board.has_bingo():
            boards.remove(board)

            last_win_score = board.sum_of_unmarked_numbers() * int(callout)
            if first_win_score is None:
                first_win_score = last_win_score

    if not len(boards):
        break

print(first_win_score)
print(last_win_score)
