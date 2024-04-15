# https://train.nzoi.org.nz/problems/1307

import sys
sys.setrecursionlimit(5000)

MAX_LENGTH = 500

I, T = map(int, input().split()) # max intensity, cloud cover time

intensities = list(map(int, input().split()))
intensities.extend(I for _ in range(MAX_LENGTH))

prefix_sums = [0] # precomputed range sums

for i in range(T + MAX_LENGTH): # prevent IndexError
    prefix_sums.append(prefix_sums[i] + intensities[i])

N, M = map(int, input().split())

dp = [[-1 for _ in range(T + 1)] for _ in range(N)] # [[-1] * I] * N
adjacency = [[] for _ in range(N)]

for i in range(M):
    line = input().split()
    start, end, time = map(int, line[:3]) # a, b, d
    adjacency[start].append((end, time, line[3] == 'S')) # edges[a] <- b, d, s

def get_cost(time, d, s):
    return 0 if s else prefix_sums[time + d] - prefix_sums[time]

def dfs(node, time):
    time = min(time, T)
    if dp[node][time] != -1:
        return dp[node][time]
    if node == N - 1: # reached destination
        dp[node][time] = 0
        return 0
    if time < T:
        dp[node][time] = dfs(node, time + 1)
    else:
        dp[node][time] = 10 ** 9 # infinity
    for end, length, shaded in adjacency[node]:
        dp[node][time] = min(dp[node][time], dfs(end, time + length) + get_cost(time, length, shaded))
    return dp[node][time]

print(dfs(0, 0))