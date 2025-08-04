E,S,M = map(int,input().split())
total = 0
e = s = m = 0
while True:
    if E == e and S == s and M == m:
        print(total)
        break
    else:
        e += 1
        s += 1
        m += 1
        total += 1
        if e == 16:
            e = 1
        if s == 29:
            s = 1
        if m == 20:
            m = 1