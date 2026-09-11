data = []
n = int(input("кол-во элементов"))
for i in range(n):
    data.append(int(input()))
res = data[-1:] + data[:-1]
print(res)