# https://train.nzoi.org.nz/problems/1323

N = 0
total = 0
grid = [[] for _ in range(3)]

for i in range(3):
    row = list(map(int, input().split()))
    count = row.count(0)
    N += count
    if count == 0:
        total = sum(row)
    grid[i] = row

for i in range(3):
    row = list(map(str, grid[i]))
    for j in range(3):
        if grid[i][j] == 0:
            grid[i][j] = total - sum(grid[i])
    row = list(map(str, grid[i]))
    print(" ".join(row))