type = input()
n = int(input())
dict = {}
for i in range(n):
  k,v = input().split(' ')
  dict[k] = v

print(dict[type])
