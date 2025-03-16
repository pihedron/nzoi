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