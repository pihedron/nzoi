N, A = map(int, input().split())

rectangles = []

for _ in range(N):
    r, c = map(int, input().split())
    rectangles.append([max(0, c - A), max(0, r - A), c + A + 1, r + A + 1])

y_events = sorted(set([y for _, a_y, _, b_y in rectangles for y in [a_y, b_y]]))

y_indexer = {
    y: i for i, y in enumerate(y_events)
}

count = [0] * len(y_indexer)

left = [(a_x, 1, a_y, b_y) for a_x, a_y, _, b_y in rectangles]
right = [(b_x, -1, a_y, b_y) for _, a_y, b_x, b_y in rectangles]

sides = sorted(left + right)

current_x = 0
y_sum = 0
area = 0

for x, event_type, a_y, b_y in sides:
    area += (x - current_x) * y_sum
    current_x = x
    for i in range(y_indexer[a_y], y_indexer[b_y]):
        count[i] += event_type
    y_sum = sum(b - a if c else 0 for a, b, c in zip(y_events, y_events[1:], count))

print(area)