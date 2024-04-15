# https://train.nzoi.org.nz/problems/1256

N, A, B = map(int, input().split())
temperatures = list(map(int, input().split()))

good_bad = []

for i in range(N):
    if A <= temperatures[i] and temperatures[i] <= B:
        good_bad.append(1)
    else:
        good_bad.append(-1)

sigma = sum(good_bad)

if sigma > 0:
    print(N)
else:
    total = 0
    best = 0
    f = {}
    for i in range(1, N + 1):
        total += good_bad[i - 1] # sum of [0:i] or first i days
        if total > 0: # [0:i] is valid
            best = max(best, i)
        elif total - 1 in f:
            # total[j] = total[i] - 1
            # total[i] - total[j] = 1
            best = max(best, i - f[total - 1]) # j = f[total - 1]
        if total not in f: # store leftmost total to increase i - j
            f[total] = i
    print(best)
