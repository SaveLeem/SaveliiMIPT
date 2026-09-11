data = []
n = int(input("кол-во элементов"))
for i in range(n):
    data.append(int(input()))
for i in range(0, n - 1, 2):
    tmp = data[i]
    data[i] = data[i + 1]
    data[i+1] = tmp
print(data)