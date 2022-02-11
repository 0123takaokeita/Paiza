x,d,k = 0,7,9
a = [x] * (k + 1)

for i in range(2, k + 1):
    a[i] = a[i - 1] + d

print(a[k])
