# https://train.nzoi.org.nz/problems/83

import heapq
import sys

n = int(input())
start, end = map(int, input().split())

adj = [[] for _ in range(n)]

def dijkstra():
    heap = [(0, start)]  # cost from start node, end node
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
        x, y = map(int, line.split())
        adj[x].append(y)
    except:
        break

if start == end:
    print(start)
else:
    print(" ".join(map(str, dijkstra())))
