n = int(input())
data = list(map(int, input().split()))

half = n // 2
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[j] < data[i]:
            cnt += 1
    if cnt == half:
        print(data[i])
        break