g = int(input())
s = input()
n = len(s) // g
new = [""] * len(s)
for i in range(0, len(s), n):
    for j in range(n):
        new[i + j] = s[i + n - 1 - j] #Mr.Deepsek напомнил про еденичку 
print("".join(new))

