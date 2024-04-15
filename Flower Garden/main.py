# https://train.nzoi.org.nz/problems/1257

N = int(input())

colours = list(input())

last = ""
replacements = 0
last_replacement = -1

for i in range(N):
    if colours[i] == last and i > last_replacement + 1:
        replacements += 1
        last_replacement = i
    last = colours[i]

print(replacements)