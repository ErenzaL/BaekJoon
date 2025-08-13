#9012
t = int(input())
for _ in range(t):
    s = input().strip().replace(" ", "")
    stack = []
    ok = True
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ')'
            if not stack:
                ok = False
                break
            stack.pop()
    print("YES" if ok and not stack else "NO")