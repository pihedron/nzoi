# https://train.nzoi.org.nz/problems/83

import heapq
import sys

n = int(input())
start, end = map(int, input().split())

adj = [[] for _ in range(n)]

def dijkstra():
    heap = [(0, start)] # start -> start has cost of 0
    visited = set()
    prev = [-1 for _ in range(n)]
    dist = [10 ** 9 for _ in range(n)]
    dist[start] = 0
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            break
        for v in adj[u]:
            if v in visited:
                continue
            alt = dist[u] + 1
            if dist[v] > alt:
                dist[v] = alt
                heapq.heappush(heap, (dist[v], v))
                prev[v] = u
    path = []
    path.append(end)
    temp = end
    while temp != start:
        temp = prev[temp]
        path.append(temp)
    path.reverse()
    return path

for line in sys.stdin:
    try:
        u, v = map(int, line.split())
        adj[u].append(v)
    except:
        break

if start == end:
    print(start)
else:
    print(" ".join(map(str, dijkstra())))
