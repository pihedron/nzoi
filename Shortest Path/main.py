# https://train.nzoi.org.nz/problems/83

import heapq
import sys

n = int(input())

start, end = map(int, input().split())

adj = [[] for _ in range(n)]
# distances = [-1 for _ in range(n)]
shortest_path = []

def dijkstra():
    heap = [(0, start)]  # cost from start node, end node
    visited = set()
    prev = [-1 for _ in range(n)]
    dist = [10 ** 9 for _ in range(n)]
    dist[start] = 0
    total_cost = -1
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            total_cost = cost
            break
        for v in adj[u]:
            if v in visited:
                continue
            # next_item = cost + 1 # cost of 1
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

# def dfs(node, nodes):
#     distance = 10 ** 9 # infinity
#     if node == end: # reached destination
#         distance = 0
#     for y in adj[node]:
#         if y in nodes: # path cyclic?
#             continue
#         if distances[y] == -1: # unexplored?
#             nodes.append(node)
#             dfs(y, nodes)
#         if distances[y] + 1 < distance:
#             global shortest_path
#             if y == end:
#                 shortest_path = copy.copy(nodes)
#                 shortest_path.append(y)
#             distance = distances[y] + 1
#         nodes.pop()
#     distances[node] = distance

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