x = ord(input())
y = ord(input())
array = []
for i in range(x,y+1):
  array.append(chr(i))

if input() in array:
  print('true')
else:
  print('false')