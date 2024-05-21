# https://train.nzoi.org.nz/problems/1306

import heapq

DP = 6

sx, sy, ex, ey = map(float, input().split())

N = int(input()) # number of shadows

vertices = [(sx, sy, 0), (ex, ey, 0)]

for i in range(N):
    x, y, r = map(float, input().split())
    vertices.append((x, y, r))

V = len(vertices)

def dijkstra():
    heap = [(0, 0)]
    visited = set()
    dist = [10 ** 9 for _ in range(V)]
    dist[0] = 0
    while heap:
        (cost, u) = heapq.heappop(heap)
        x, y, r = vertices[u]
        if u in visited:
            continue
        visited.add(u)
        if x == ex and y == ey:
            break
        for v in range(1, V):
            if v in visited or v == u:
                continue
            dx = vertices[v][0] - x
            dy = vertices[v][1] - y
            w = max(0, (dx ** 2 + dy ** 2) ** 0.5 - r - vertices[v][2])
            alt = cost + w
            if dist[v] > alt:
                dist[v] = alt
                heapq.heappush(heap, (dist[v], v))
    return dist[1]

print(round(dijkstra(), DP))