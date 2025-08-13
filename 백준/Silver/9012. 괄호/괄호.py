t = int(input())
results = []  

for _ in range(t):
    s = input().strip().replace(" ", "")
    bal = 0
    ok = True
    for ch in s:
        if ch == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            ok = False
            break
    results.append("YES" if ok and bal == 0 else "NO")

print("\n".join(results))