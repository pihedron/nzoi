# https://train.nzoi.org.nz/problems/1274

N, M, V_A, V_B = map(int, input().split())

A_deps = input().split()

A = [[] for _ in range(V_A)] # int[V_A][N]

for v in range(V_A):
    A[v] = list(map(int, input().split()))

B_deps = input().split()

B = [[] for _ in range(V_B)] # int[V_B][M]

for v in range(V_B):
    B[v] = list(map(int, input().split()))

common = []
v_a = V_A - 1
v_b = V_B - 1

for a in range(N):
    for b in range(M):
        if A_deps[a] == B_deps[b]:
            common.append((a, b))

def find_common(v_a, v_b):
    for i in reversed(range(V_A)):
        for j in reversed(range(V_B)):
            if A[i][a] == B[j][b]:
                return (min(v_a, i), min(v_b, j))

for c in common:
    a, b = c
    v_a, v_b = find_common(v_a, v_b)

print(v_a, v_b)