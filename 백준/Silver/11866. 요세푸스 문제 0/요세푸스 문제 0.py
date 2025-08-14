#11866
N, K = map(int, input().split())
people= list(range(1,N+1))
order = []
idx = 0

while people:
    idx = (idx + K -1) % len(people)
    order.append(people.pop(idx))

print("<" + ", ".join(map(str, order)) + ">")