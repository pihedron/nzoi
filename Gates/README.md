# Solution

## Subtask

When a plane lands it can dock at any gate from 1 to $g_i$. This removes 1 docking possibility for all gates greater than or equal to $g_i$.

```py
G = int(input())
P = int(input())

g = [0] * P
gates = [0] * G

for i in range(P):
    g[i] = int(input()) - 1

count = 0

for i in range(P):
    if gates[g[i]] == g[i] + 1:
        break

    for j in range(g[i], G):
        gates[j] += 1

    count += 1

print(count)
```

## Full

There are many ways to fully solve this problem but the simplest solution is to use a disjoint set.

For each gate, we want to keep track of the highest unoccupied gate. When a plane docks at gate $g_i$, the gate $g_i$ is united with $g_{i-1}$. This will redirect any queries for $g_i$ to $g_{i-1}$.

```py
G = int(input())
P = int(input())

g = [0] * P
empty = [True] * G

for i in range(P):
    g[i] = int(input()) - 1

count = 0

parent = [j for j in range(G)]

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

for i in range(P):
    gate = find(g[i])

    if not empty[gate]: break

    empty[gate] = False
    count += 1
    parent[gate] = find(max(0, gate - 1))

print(count)
```