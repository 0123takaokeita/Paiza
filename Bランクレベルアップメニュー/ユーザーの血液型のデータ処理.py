n = int(input())
dict = {}
for i in range(n):
  k,v = input().split(' ')
  dict[k] = v
  print(f"{k} {v}")
