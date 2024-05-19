sx, sy, ex, ey = map(int, input().split())

N = int(input()) # number of shadows

vertices = []

for i in range(N):
    x, y, r = map(int, input().split())
    vertices.append((x, y))

