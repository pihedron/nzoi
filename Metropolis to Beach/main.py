# https://train.nzoi.org.nz/problems/1328

N = int(input())

total = 0
max_total = -1

for i in range(N):
    delta = int(input())
    if delta > 0:
        total += delta
        max_total = max(max_total, total)
    else:
        total = 0

print(max_total)