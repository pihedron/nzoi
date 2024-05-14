# Problem

Read in a directed graph which has been described as a list of edges, a source and a destination vertex and then output the shortest path between the source and the destination.

An extra rule so that your results can be easily compared:
At any point if there is a choice of which vertex to visit, visit them in ascending numerical order

Eg: if a vertex's neighbours are 5, 2, 7 and 3 process them in the order 2, 3, 5 then 7.

## Input
Each vertex will be represented as a number from 0 to n-1 for n vertices.
The first line of input will state how many vertices are in the graph
The second line will specify the start and destination vertices
Each subsequent line will consist of pairs of numbers each describing an edge. The first number in the pair describes the vertex from where the edge originates and the second number states the vertex where the edge leads to.
The list will end with the end of the file.

## Output
Output the shortest path from the source to the destination as a list of vertices, on one line, separated by spaces.

## Constraints
1 <= n <= 1,000,000 and 0 <= total number of edges <= 1,000,000

## Sample Input 1
```
3
2 1
0 1
1 0
1 2
0 2
2 0
```

## Sample Output 1
```
2 0 1
```
 
## Sample Input 2
```
10
5 5
1 2
2 3
```

## Sample Output 2
```
5
```

# Solution

This problem involves a *directed* **graph** which means we only need to update the adjacency list for the first vertex in each input line.

```py
n = int(input())
start, end = map(int, input().split())

adj = [[] for _ in range(n)]

# this problem requires a goofy input reader
for line in sys.stdin:
    try:
        x, y = map(int, line.split())
        adj[x].append(y)
    except:
        break
```

The goal is to find the shortest path and all the edges have an equal *distance* or *weighting*. Therefore, Dijkstra's algorithm with a priority queue can be used to find the shortest path. Note that this graph could be **cyclic**, meaning DFS is not a suitable algorithm. 

```py
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
```

The cost or weight of the edge is at index 0 of the tuple to give priority to items based on their cost in the priority queue. The cost variable is mostly unused because all edges have the same weight of 1.