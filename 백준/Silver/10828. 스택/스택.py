#10828
t = int(input())
results = []
stack = []
for _ in range(t):
    s = input().strip().split()
    if 'push' in s[0]:
        stack.append(int(s[1]))

    elif s[0] == "pop":
        results.append(stack.pop() if stack else -1)

    elif s[0] == "size":
        results.append(len(stack))

    elif s[0] == "empty":
        results.append(0 if stack else 1)

    elif s[0] == "top":
        results.append(stack[-1] if stack else -1)

# 한 번에 출력
print("\n".join(map(str, results)))