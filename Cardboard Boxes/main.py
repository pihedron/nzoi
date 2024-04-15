N = int(input())

boxes = []

for i in range(N):
    boxes.append(int(input()))

boxes.sort()

last_box = boxes[0]
total = 1

for i in range(1, N):
    if boxes[i] != last_box:
        last_box = boxes[i]
        total += 1

print(total)