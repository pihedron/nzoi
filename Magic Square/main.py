# https://train.nzoi.org.nz/problems/1323

N = 0
SIDE = 3
MAX = 10000

grid = [] # flat grid
corners = [
    0,
    SIDE - 1,
    (SIDE - 1) * SIDE,
    SIDE ** 2 - 1,
]
magic_total = 0
rays = []

# horizontal
for i in range(3):
    rays.append((i * SIDE, 1))

# vertical
for i in range(3):
    rays.append((i, SIDE))

# diagonal
rays.append((0, SIDE + 1))
rays.append((2, SIDE - 1))

def print_grid(grid):
    for i in range(SIDE ** 2):
        char = "\n" if i % SIDE == SIDE - 1 else " "
        print(grid[i], end=char)

for i in range(SIDE):
    row = list(map(int, input().split()))
    count = row.count(0)
    N += count

    if count == 0:
        magic_total = sum(row)

    grid.extend(row)

def corners_are_missing_from(square):
    for corner in corners:
        if square[corner] != 0:
            return False

    return True

def solve_trivial():
    for i in range(SIDE ** 2):
        if grid[i] == 0:
            row_index = i // SIDE
            row = grid[slice(row_index * SIDE, (row_index + 1) * SIDE)]

            if row.count(0) == 1:
                grid[i] = magic_total - sum(row)
                break

            col_index = i % SIDE
            col = grid[slice(col_index, SIDE ** 2, SIDE)]

            if col.count(0) == 1:
                grid[i] = magic_total - sum(col)
                break

if N <= 2:
    while grid.count(0) > 0:
        solve_trivial()

    print_grid(grid)
else:
    for target in range(SIDE, SIDE * MAX):
        valid = True
        square = grid.copy()
        done = False

        while True:
            for ray in rays:
                total = 0
                zeros = 0

                index, step = ray
                i = index

                for _ in range(SIDE):
                    total += square[i]

                    if square[i] == 0:
                        zeros += 1
                        last_zero = i
                    
                    i += step

                if zeros == 1:
                    guess = target - total

                    if not 1 <= guess <= MAX:
                        valid = False

                    square[last_zero] = guess
                elif zeros == 0:
                    if total != target:
                        valid = False
                
            if done: break

            if not valid or 0 not in square:
                done = True
            
            if valid and corners_are_missing_from(square):
                square[corners[0]] = (target - square[SIDE ** 2 // 2] + square[SIDE + SIDE - 1] - square[SIDE // 2]) // 2
                square[corners[1]] = target - square[SIDE // 2] - square[corners[0]]
                square[corners[3]] = target - square[SIDE + SIDE - 1] - square[corners[1]]
                square[corners[2]] = target - square[(SIDE - 1) * SIDE + 1] - square[corners[3]]

        if valid:
            print_grid(square)
            break