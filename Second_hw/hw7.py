data = []
n = int(input("кол-во элементов"))
for i in range(n):
    data.append(int(input()))
max = -1
for i in range(len(data)):
    cnt = 0
    for j in range(len(data)):
        if data[i] == data[j]:
            cnt += 1
    if (cnt > max):
        max = i
print(data[max])