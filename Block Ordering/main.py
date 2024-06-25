# https://train.nzoi.org.nz/problems/1242

import math

N = int(input())

chunks = []
chunk = 0 # < 8

for _ in range(N):
    block = input()
    if block == "o":
        chunk += 1
    elif block == "a":
        pass
    elif block == "r":
        pass
    else: # block == "s"
        chunks.append(chunk)
        chunk = 0

chunks.append(chunk)

def solve_chunk():
    pass

permutations = 1

for c in chunks:
    permutations *= math.factorial(c)

print(permutations % (10 ** 9 + 7))