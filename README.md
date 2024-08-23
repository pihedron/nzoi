# NZOI Solutions

This project contains solutions to some of the problems on the [NZOI Training Website](https://train.nzoi.org.nz).

## Languages

I solved most of the problems using Python, but for some of them I used C#, JavaScript, or Java. It is better to use Java or C++ because they are the standard choice for the International Olympiad in Informatics.

## Time Complexity

For some graph problems like **Sunsprint**, Python is not fast enough to complete all subtasks. Each folder may contain a `README.md` file for guidance on the problem.

## Common Algorithms

### Dijkstra

```py
def dijkstra(adj, n, start, end):
    heap = [(0, start)]
    visited = [False] * n
    dist = [10 ** 9 for _ in range(n)]
    dist[start] = 0
    while heap:
        (d, u) = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if u == end:
            break
        for (v, w) in adj[u]:
            if visited[v]:
                continue
            d += w
            if dist[v] > d:
                dist[v] = d
                heapq.heappush(heap, (dist[v], v))
    return dist[end]
```