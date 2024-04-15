# https://train.nzoi.org.nz/problems/1238

import sys
import heapq

def anti_dijkstra(graph, anti_nodes):
    heap = anti_nodes

    while heap:
        (cost, current) = heapq.heappop(heap)

        if cost == M:
            continue

        if visited[current]:
            continue

        visited[current] = True

        for adjacent, weight in graph[current]: # iterate outgoing edges
            if visited[adjacent]:
                continue

            heapq.heappush(heap, (cost + weight, adjacent))

def dijkstra(graph, start, end):
    count = len(graph)
    heap = [(0, start)] # priority queue (cost, node)

    costs = [sys.maxsize for _ in range(count)] # set the cost to infinity for all vertices
    costs[start] = 0
    
    total_cost = -1

    while heap:
        (cost, current) = heapq.heappop(heap)

        if visited[current]:
            continue

        visited[current] = True

        if current == end:
            total_cost = cost
            break

        for adjacent, weight in graph[current]: # iterate outgoing edges
            if visited[adjacent]:
                continue

            alt = costs[current] + weight
            
            if costs[adjacent] > alt:
                costs[adjacent] = alt
                heapq.heappush(heap, (costs[adjacent], adjacent))

    return total_cost

N, E = map(int, input().split()) # number of vertices, edges
graph = [[] for _ in range(N)]
visited = [False] * N

for i in range(E):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # weight of 1
    graph[b].append((a, 1)) # weight of 1

S, M = map(int, input().split())

shoppers = []

for i in range(S):
    node = int(input())
    shoppers.append((0, node))

anti_dijkstra(graph, shoppers)

cost = dijkstra(graph, 0, N - 1)
print("SELF_ISOLATE" if cost < 0 else cost + 1)