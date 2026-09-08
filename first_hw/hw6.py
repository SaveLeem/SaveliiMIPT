f = open('input.txt', 'r')
data = f.read()
f.close()
lines = data.split('\n')
nums = lines[0].split()
op = lines[1].strip()
base = int(lines[2])
base10 = 10
def change_base(n, base, alph="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if n == 0:
        return "0"
    if n < 0:
        n = -n
    result = ""
    while n > 0:
        ost = n % base
        result = alph[ost] + result
        n = n // base
    return "-" + result if n < 0 else result

def change_back(n, base, alph="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    N=str(n)
    L=list(N)
    for i in range(len(L)):
        if L[i] in alph[0:10]:
            L[i]=int(L[i])
        else:
            index = alph.find(L[i])
            L[i] = index + 10
    resultB=0
    for i in range(len(L)):
        resultB = resultB + int(L[i])*base**(len(L)-i-1)
    return resultB
nums10 = []
for i in range(len(nums)):
    nums10.append(change_back(nums[i], base))
sum10 = sum(nums10)
Result = change_base(sum10, base)
f = open('output.txt', 'w')
f.write(Result)
f.close()
