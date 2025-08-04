n = int(input())
sum = 0
result = []
for i in range(n):
    a,b = map(int, input().split())
    sum = a+b
    result.append(sum)

for t in range(1,n+1):
    index = t-1
    print(f'Case #{t}: {result[index]}')