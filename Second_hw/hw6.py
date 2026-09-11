data = []
n = int(input("кол-во элементов"))
for i in range(n):
    data.append(int(input()))

for i in range(len(data)):
    cnt = 0
    for j in range(len(data)):
        if i != j and data[i] == data[j]:
            cnt += 1
    if cnt == 0: #встречается 1 раз
        print(data[i], end=" ")