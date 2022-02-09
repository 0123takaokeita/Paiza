name = input()
n = int(input())
user = {}
for i in range(n):
  k,v = input().split(' ')
  user[k] = v

n = int(input())
result = {}
for i in range(n):
  k,v = input().split(' ')
  result[k] = v

print(result[user[name]])



