list = list(map(str,range(0,365,1)))
n = input()
count = 0
for i in list:
  if n in i:
    count += 1
    # print(i)

print(count)
