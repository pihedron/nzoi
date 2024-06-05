# https://train.nzoi.org.nz/problems/1169

N, X, M = map(int, input().split())

k = [] # max occupants
h = [] # starting house
d = [] # max distance

adj = [[] for _ in range(M)]
trivial = True

for i in range(N):
    k_i = int(input())
    k.append(k_i)

for j in range(M):
    h_j, d_j = map(int, input().split())
    h.append(h_j - 1) # convert to 0 indexed
    d.append(d_j // X)

for j in range(M):
    for i in range(N):
        if k[i] == 0:
            continue
        if abs(h[j] - i) <= d[j]:
            adj[j].append(i)

p = sorted(range(M), key=lambda j: len(adj[j]))

for j in p:
    if not trivial:
        break
    trivial = False
    for i in adj[j]:
        if k[i] == 0:
            continue
        trivial = True
        k[i] -= 1
        h[j] = i

if trivial:
    print("SOLUTION IS TRIVIAL")
    for i in h:
        print(i + 1)
else:
    print("SOLUTION IS NON-TRIVIAL")