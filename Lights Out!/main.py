# https://train.nzoi.org.nz/problems/1272

N = int(input())
M = int(input())

s = [0 for _ in range(N)]

for m in range(M):
    for n in range(m, N, m + 1):
        s[n] += 1
        s[n] %= 2

print(sum(s))