import heapq

sx, sy, ex, ey = map(float, input().split())

N = int(input()) # number of shadows

vertices = [(sx, sy), (ex, ey)]

for i in range(N):
    x, y, r = map(float, input().split())
    vertices.append((x, y))

def dijkstra():
    heap = [(0, 0)]
    visited = set()
    dist = [10 ** 9 for _ in range(N)]
    dist[0] = 0
    while heap:
        (cost, u) = heapq.heappop(heap)
        x, y = vertices[u]
        if u in visited:
            continue
        visited.add(u)
        if x == ex and y == ey:
            break
        for v in range(1, N):
            if v in visited or v == u:
                continue
            dx = vertices[v][0] - x
            dy = vertices[v][1] - y
            w = (dx ** 2 + dy ** 2) ** 0.5
            alt = cost + w
            if dist[v] > alt:
                dist[v] = alt
                heapq.heappush(heap, (dist[v], v))
    return dist[1]

print(dijkstra())