# https://train.nzoi.org.nz/problems/1270

N = int(input())

s = list(map(int, input().split()))
s.sort()

pairs = []

for i in range(N // 2):
    pairs.append((s[i], s[N - i - 1]))

pairs.sort(key = lambda x: sum(x))

print(sum(pairs[-1]) - sum(pairs[0]))