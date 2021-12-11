import sys

grid = [[int(field) for field in row.strip()] for row in sys.stdin]

field_count = sum(len(row) for row in grid)
flash_count = 0
first_synchronized_flash = None

step = 0
while first_synchronized_flash is None or step <= 100:
    step += 1
    flashes = set()
    queue = set()

    # Increase power level per field
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1

            if grid[y][x] > 9:
                flashes.add((x, y))
                queue.add((x, y))

    # Trigger subsequent flashes
    while queue:
        (x, y) = queue.pop()

        for ny in range(max(0, y-1), min(len(grid), y+2)):
            for nx in range(max(0, x-1), min(len(grid[ny]), x+2)):
                neighbor = (nx, ny)

                grid[neighbor[1]][neighbor[0]] += 1

                if grid[neighbor[1]][neighbor[0]] > 9 and neighbor not in flashes:
                    flashes.add(neighbor)
                    queue.add(neighbor)

    # Reset power level to 0 for flashing fields
    for (x, y) in flashes:
        grid[y][x] = 0

    # Keep track of flashing statistics
    flash_count += len(flashes) if step <= 100 else 0

    if first_synchronized_flash is None and len(flashes) == field_count:
        first_synchronized_flash = step

print(flash_count)
print(first_synchronized_flash)
