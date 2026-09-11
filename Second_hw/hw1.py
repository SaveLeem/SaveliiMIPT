n = int(input('первое число'))
data = [n]
for i in range(n - 1):
    data.append(int(input()))
real_summ = sum(data) - data[0]
exp_summ = 0
for i in range(1, n + 1):
    exp_summ += i
lost_card = exp_summ - real_summ
print(lost_card)