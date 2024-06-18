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

def versions_match(i, j):
    for a, b in common:
        if A[i][a] != B[j][b]:
            return False
    return True

def find_latest_version():
    for i in reversed(range(V_A)):
        for j in reversed(range(V_B)):
            if versions_match(i, j):
                return i, j

v_a, v_b = find_latest_version()

print(v_a, v_b)