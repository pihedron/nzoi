X, Y, A, B = map(int, input().split())

a = (X // A) * (Y // B)
b = (X // B) * (Y // A)

print(max(a, b))