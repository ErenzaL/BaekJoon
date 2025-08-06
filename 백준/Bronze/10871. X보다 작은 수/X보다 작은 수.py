N, X = map(int, input().split())
#input N numbers
A = list(map(int, input().split()))
result = [str(num) for num in A if num < X]
print(" ".join(result))