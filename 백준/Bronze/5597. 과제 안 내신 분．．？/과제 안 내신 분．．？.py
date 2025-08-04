students = list(range(1,31))
handed = []
for i in range(28):
    a = int(input())
    handed.append(a)

not_handed = [s for s in students if s not in handed]

for s in not_handed:
    print(s)