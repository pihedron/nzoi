N = int(input())
h = list(map(int, input().split()))

unsafe = [True] * N
count = 0
stack = []

for i in range(N):
    while stack and h[stack[-1]] < h[i]:
        stack.pop() # shorter towers not visible
    
    last = stack[-1] if stack else None

    if stack and h[last] == h[i]:
        if unsafe[last]:
            unsafe[last] = False
            count -= 1
        
        unsafe[i] = False
    else:
        count += 1
    
    stack.append(i)
    print(count)