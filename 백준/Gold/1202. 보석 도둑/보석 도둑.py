import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]  # (M, V)
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: x[0])  
bags.sort()

ans = 0
hq = []            
i = 0              # diamond index

for c in bags:     # 작은 가방부터
    while i < N and jewels[i][0] <= c:
        heapq.heappush(hq, -jewels[i][1])  
        i += 1
    if hq:
        ans += -heapq.heappop(hq)          # choose higher price diamond

print(ans)