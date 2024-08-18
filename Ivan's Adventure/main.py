from math import ceil, sqrt

N, M = map(int, input().split())

cities = [tuple(map(int, input().split())) for _ in range(N)]
path = list(map(int, input().split()))

def cost(city_a, city_b):
    return ceil(sqrt((city_a[0] - city_b[0]) * (city_a[0] - city_b[0]) + (city_a[1] - city_b[1]) * (city_a[1] - city_b[1])))

money = [0] * M

for i in range(M - 2, -1, -1):
    money[i] = money[i + 1] + cost(cities[path[i]], cities[path[i + 1]]) # prefix sum

new_unreachable = [0] * (M + 1)

for city in cities:
    # binary search
    low = 0
    high = M
    while low != high:
        middle = (low + high) // 2
        if cost(cities[path[middle]], city) <= money[middle]:
            low = middle + 1
        else:
            high = middle
    new_unreachable[low] += 1

ans = N - 1

for i in range(M):
    ans -= new_unreachable[i]
    print(ans, end=" ")

print() # line break