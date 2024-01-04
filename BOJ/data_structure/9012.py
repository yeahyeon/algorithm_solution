import sys

t = int(input())

for _ in range(t):
    stack = []
    line = sys.stdin.readline().strip()
    for i in line:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                stack.pop()
        
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
