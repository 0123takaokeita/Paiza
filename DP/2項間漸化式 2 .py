# x, d = map(int, input().split())
x,d = 0,7
a = [x] * (1000 + 1)
for i in range(2, 1000 + 1):
    a[i] = a[i - 1] + d

# q = int(input())
q = 9
print(a)
for i in range(q):
    k = int(input())
    print(a[k])