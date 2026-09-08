import numpy as np
a = int(input("Натуральное число"))
b = len(str(a))
d = []
for char in str(a):
    d.append(int(char))
arr = np.array(d)
print(d[b-1])