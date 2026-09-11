f = open('input.txt', 'r')
data = f.read()
f.close()

cnt = 0
for i in range(len(data)):
    if data[i] in ".!?" and (i == 0 or data[i-1] not in ".!?"):
            cnt += 1
print(cnt)