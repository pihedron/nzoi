# https://train.nzoi.org.nz/problems/629

N = int(input())

nums = list(map(int, input().split()))
piles = [nums[0]]

for i in range(1, N):
    min_pile = 10 ** 9
    index = -1
    for j in range(len(piles)):
        if nums[i] <= piles[j]:
            if piles[j] < min_pile:
                min_pile = piles[j]
                index = j
    if index >= 0:
        piles[index] = nums[i]
    else:
        piles.append(nums[i])
        

print(len(piles))