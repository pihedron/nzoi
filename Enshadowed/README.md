# Problem

It's yet another sweltering day at the University of Canterbury. Roxy needs to get between her lectures, and wants to stay out of the sun as much as possible.

Luckily, there are some trees on campus providing delicious shade. The university keeps their grounds meticulously maintained, and the treetops are topiaried into perfect spheres. The shadows of the trees are thus all circular in shape. (The trunks of the trees also happen to be infinitesimally thin, thus casting no shadow). The campus grounds are famously flat, so assume all distances are on a flat 2D plane.

Given Roxy's position and destination, and the centers and radii of the shadows, output the minimum distance Roxy must travel in the sun to get to her lecture.

# Input
The first line contains 4 space-separated numbers, xR yR xL yL, where (xR,yR) are Roxy's (Cartesian) coordinates and (xL,yL) are the coordinates of her destination. The second line contains a single integer N, the number of shadows. The following N lines each contain three space separated numbers, xC yC r, indicating there is a shadow centered at (xC,yC) with radius r.

# Output
Output a single floating-point number, the minimum distance Roxy must travel in the sun. You must output the distance within a 10−4 error.

# Constraints
−1000≤xR,yR,xL,yL,xC,yC≤1000
0≤r≤1000
1≤N≤500
Subtasks
Subtask 1 (+20%): N=1
Subtask 2 (+30%): N≤20
Subtask 3 (+50%): No further constraints.
Note
For students using C++, std::cout by default does not print floating-point numbers with enough precision to pass the test data. Instead use printf or set the precision manually with std::cout.precision().

# Sample Input 1
```
0.0 0.0 4.0 0.0
1
2.0 0.0 1.0
```
# Sample Output 1
```
2.000000
```
 
# Sample Input 2
```
0.0 1.0 20.0 -6.0
3
-1.0 -2.0 1.0
4.0 2.0 3.0
7.0 -6.0 2.0
```
# Sample Output 2
```
15.667109
```

# Solution

This problem is a minor twist on the shortest path problem. All the shadows including the start and end points are nodes on a graph. It is important to note that we are dealing with a **complete graph** because Roxy can walk from any node to any other node. The only exception would be the start node because walking back to where she started would only result in Roxy travelling a longer distance than necessary.

A list of vertices instead of an adjacency list is enough to represent the graph because the distances can be calculated using the Pythagorean theorem and the x, y, and r values of the vertices.

> [!NOTE]
> The start and end nodes have a radius of 0 because they do not have any shadows.

```
sx, sy, ex, ey = map(float, input().split())

N = int(input()) # number of shadows

vertices = [(sx, sy, 0), (ex, ey, 0)]

for i in range(N):
    x, y, r = map(float, input().split())
    vertices.append((x, y, r))

V = len(vertices)
```

Since being in the shade does not count as walking in the sun, the weight of each edge is the distance between the nodes minus the sum of their radii. However, this formula can result in negative edge weights and provide an incorrect answer when shadows intersect. Therefore, the edge weight should be corrected to 0 whenever it is less than 0.