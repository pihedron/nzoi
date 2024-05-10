# https://train.nzoi.org.nz/problems/1318

from itertools import permutations

N = int(input())
a_values = []
friends = set()

for i in range(N):
    a, b = map(int, input().split())
    a_values.append(a)
    friends.add((a, b))

for order in permutations(a_values):
    friended = set()
    friends_made = set()
    for x in order:
        friend = 2 * x
        while friend in friended:
            friend += x
        friended.add(x)
        friended.add(friend)
        friends_made.add((x, friend))
    if friends_made == friends:
        print(*order)
        break