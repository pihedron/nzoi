# https://train.nzoi.org.nz/problems/1040

N, M, K = map(int, input().split())

s = [] # speeds
x = [] # people

for i in range(N):
    s.append(int(input()))

for i in range(M):
    x.append(int(input()))

if K == M:
    print(N)
else:
    x.sort()
    max_speed = x[K]

    pref = [0]

    for i in range(N):
        pref.append(pref[i] + s[i])

    num_sections = 0

    for init_speed in range(max_speed):
        i = 1
        while i <= N and init_speed + pref[i] > 0 and init_speed + pref[i] <= max_speed:
            num_sections = max(num_sections, i)
            i += 1
        if i > N:
            continue
        if init_speed + pref[i] == 0:
            num_sections = max(num_sections, i + 1)
        if init_speed + pref[i] >= max_speed:
            break

    print(num_sections)