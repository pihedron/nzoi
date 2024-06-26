# https://train.nzoi.org.nz/problems/1242

import math
import itertools

N = int(input())

chunks = []
chunk = [] # len(chunk) < 8

for _ in range(N):
    block = input()
    if block == "s":
        chunks.append(chunk)
        chunk = []
    else:
        chunk.append(block)

chunks.append(chunk)

def arrangement_valid(c, arrangement, bounds):
    for i, id in enumerate(arrangement):
        if not bounds[id][0] < i < bounds[id][1]:
            return False
        block = c[id]
        if block == "a":
            if i > id:
                return False
        if block == "r":
            if i < id:
                return False
    return True

def solve_chunk(c):
    if len(c) <= 1:
        return 1
    bounds = [[0, len(c)] for _ in c]
    left = -1
    right = len(c)
    for i, block in enumerate(c):
        bounds[i][0] = left
        if block == "a":
            left = i
    for j, block in enumerate(reversed(c)):
        i = len(c) - j - 1 # reversed iteration
        bounds[i][1] = right
        if block == "r":
            right = i
    arrangements = list(itertools.permutations(range(len(c))))
    permutations = 0
    for arrangement in arrangements:
        if arrangement_valid(c, arrangement, bounds):
            permutations += 1
    return permutations

permutations = 1

for c in chunks:
    permutations *= solve_chunk(c)

print(permutations % (10 ** 9 + 7))