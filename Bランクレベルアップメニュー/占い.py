
def make_dict(n,dict):
  for i in range(n):
    k,v = input().split(' ')
    dict[k] = v
  return dict


user = make_dict(int(input()),{})
result = make_dict(int(input()),{})

for i in user:
  print(f"{i} {result[user[i]]}")  



