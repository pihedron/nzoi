# https://train.nzoi.org.nz/problems/1241

N = int(input())

W = []
A = []
X = []
B = []
Y = []

for _ in range(N):
    w, a, x, b, y = map(int, input().split())
    W.append(w)
    A.append(a)
    X.append(x)
    B.append(b)
    Y.append(y)

cost = 0

for i in range(N):
    if X[i] > Y[i]:
        amt = min(W[i], B[i])
        cost += amt * Y[i]
        cost += (W[i] - amt) * X[i]
    elif X[i] < Y[i]:
        amt = min(W[i], A[i])
        cost += amt * X[i]
        cost += (W[i] - amt) * Y[i]
    else:
        cost += W[i] * X[i]

print(cost)