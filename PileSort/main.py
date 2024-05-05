# https://train.nzoi.org.nz/problems/629

import bisect

N = int(input())
piles = []

for num in list(map(int, input().split())):
    index = bisect.bisect_left(piles, num)
    if index < len(piles):
        piles[index] = num
    else:
        piles.append(num)

print(len(piles))