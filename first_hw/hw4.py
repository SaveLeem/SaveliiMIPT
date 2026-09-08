f = open('input.txt', 'r')
data = f.read()
f.close()
lines = data.split('\n')
nums = list(map(int, lines[0].split()))
op = lines[1].strip()
if op == "+":
    res = sum(nums)
elif op == "-":
    res = res = 2 * nums[0] - sum(nums)
elif op == '*':
    res = 1
    for x in nums:
        res *= x
f = open('output.txt', 'w')
f.write(str(res))
f.close
