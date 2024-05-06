# https://train.nzoi.org.nz/problems/1322

import math

N = int(input())
nums = list(map(int, input().split()))

print(math.ceil(sum(nums) / len(nums)) * len(nums) - sum(nums))