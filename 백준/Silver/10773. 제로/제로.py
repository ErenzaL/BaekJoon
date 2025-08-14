#10773
n = int(input())
statement = []
for i in range(n):
    num = int(input())
    statement.append(num)

list_num = []
for i in range(len(statement)):
    if statement[i] !=0 :
        list_num.append(statement[i])
    else:
        list_num.pop()
total = sum(list_num)
print(total)