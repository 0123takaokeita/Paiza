n = int(input())
dic = {}
for i in range(n):
  x,y = input().split()
  dic[int(y)] = x

sorted = sorted(dic.keys())
for i in sorted:
  print(dic[i])
