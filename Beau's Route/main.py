N = int(input())

route = []
step = N // 2

def solve_even(a, b):
    for i in range(a):
        if i % 2 == 0:
            route.append(step - i // 2)
        else:
            route.append(b - i // 2)

if N % 2 == 0:
    solve_even(N, N)
else:
    for i in range(0, N, step):
        route.append(i + 1)
    solve_even(N - 3, N - 1)

print(*route)