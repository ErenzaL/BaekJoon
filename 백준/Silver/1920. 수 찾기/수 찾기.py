#1920
N = int(input())
A = set(map(int, input().split())) # N 개
M = int(input())
B = list(map(int, input().split())) # M 개

for i in range(len(B)):
    if B[i] in A:
        print(1)
    else:
        print(0)