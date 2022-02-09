board = []
for i in range(5):
  board.append(input())
result = ''
for i in board:
  if i.count('O') == 5:
    result = 'O'
  elif i.count('X') == 5:
    result = 'X'

if result == '':
  print('D')
else:
  print(result)
