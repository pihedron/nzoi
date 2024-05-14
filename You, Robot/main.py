# https://train.nzoi.org.nz/problems/1034

import heapq

N, P, S, E = map(int, input().split())

adj = [[] for _ in range(N)]

def dijkstra():
    heap = [(0, S)]
    visited = set()
    dist = [10 ** 9 for _ in range(N)]
    dist[S] = 0
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == E:
            break
        for v in adj[u]:
            if v in visited:
                continue
            alt = dist[u] + 1
            if dist[v] > alt:
                dist[v] = alt
                heapq.heappush(heap, (dist[v], v))
    return dist[E]

for _ in range(P):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

print(dijkstra())