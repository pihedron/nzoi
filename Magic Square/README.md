# Problem

A magic square is a square grid of numbers where the sums of each row, column, and both diagonals are the same.

You will be given a 3x3 magic square of positive integers. However, the magic square is incomplete – there are $N$ missing elements, denoted by the value $0$.

Solve the magic square.

## Input
There will be three lines, each containing three space-separated integers, representing elements of the incomplete magic square.

Exactly $N$ of the elements will be $0$, indicating a missing value that must be found. All remaining elements will be between $1$ and $10000$ (inclusive).

## Output
You should print three lines, each containing three space-separated integers, representing elements of the completed magic square.

It is guaranteed that there is a unique solution, and that all elements of the solution will be between $1$ and $10000$ (inclusive).

## Subtasks
Subtask 1 (25%): $N=1$
Subtask 2 (25%): $1\le N\le 2$
Subtask 3 (25%): $1\le N\le 3$
Subtask 4 (25%): $1\le N\le 5$
## Sample Input 1
```
3 3 6
7 0 1
2 5 5
```
## Sample Output 1
```
3 3 6
7 4 1
2 5 5
``` 
## Sample Input 2
```
6 1 0
7 0 3
0 9 4
```
## Sample Output 2
```
6 1 8
7 5 3
2 9 4
```

## Solution

This problem requires a combination of bruteforce and mathematics to solve the magic square efficiently. After drawing a few incomplete magic squares, it becomes clear which squares can be solved quickly and which squares need guessing.

When N \le  2, the solution is trivial because the square is guaranteed to have at least 1 complete line where the target sum or the *magic total* can be calculated. 

```py
N = 0
grid = [] # flat grid
magic_total = 0
totals = []

for i in range(3):
    row = list(map(int, input().split()))
    count = row.count(0)
    N += count
    if count == 0:
        magic_total = sum(row)
    grid.extend(row)

def solve_trivial():
    for i in range(9):
        if grid[i] == 0:
            row_index = i // 3
            row = grid[slice(row_index * 3, (row_index + 1) * 3)]
            if row.count(0) == 1:
                grid[i] = magic_total - sum(row)
                break
            col_index = i % 3
            col = grid[slice(col_index, 9, 3)]
            if col.count(0) == 1:
                grid[i] = magic_total - sum(col)
                break

while grid.count(0) > 0:
    solve_trivial()

for i in range(9):
    char = "\n" if i % 3 == 2 else " "
    print(grid[i], end=char)
```

When N = 3, we run into a problem as seen in the 2nd sample input. When a whole diagonal is missing, it is impossible to extract a *magic total*. Therefore, bruteforce is required. Since it is very quick to solve a magic square with a when *magic total* is given, we can generate all the possible target sums and attempt to solve the square. This means we will have to check if the square is valid as well before printing the solution.

> [!NOTE]
> Each line only has to be iterated over twice because all lines would have been filled in the 1st iteration.

```py
N = 0
SIDE = 3
MAX = 10000

grid = [] # flat grid
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

        for _ in range(2):
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

        if valid:
            print_grid(square)
            break
```

For the full solution, there is another edge case that needs to be dealt with. When all the corners are missing, all the 6 unsolved lines have 2 blanks. This means subtracting from the target sum to get a value is impossible but each corner can be solved using a system of 4 equations.