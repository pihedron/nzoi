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
    heap = [(0, start)] # distance to start is 0
    visited = set()
    dist = [10 ** 9 for _ in range(n)] # set all distances from start to infinity
    dist[start] = 0
    while heap:
        (w, u) = heapq.heappop(heap)
        if u in visited: # already visited node
            continue
        visited.add(u)
        if u == end: # end reached
            break
        for v in adj[u]: # iterate outgoing edges
            if v in visited:
                continue
            d = dist[u] + w # distance from start
            if dist[v] > d:
                dist[v] = d
                heapq.heappush(heap, (dist[v], v))
    return dist[end]
```