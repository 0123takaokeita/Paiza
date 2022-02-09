def judge(board):
  result = ''
  for i in board:
    if i.count('O') == 5:
      result = 'O'
    elif i.count('X') == 5:
      result = 'X'

  if result == '':
    return('D')
  else:
    return(result)


board = []
rboard = []
for i in range(5):
  board.append(input())

for i in range(5):
  r_str = ''
  for j in range(5):
    r_str += board[j][i]
  rboard.append(r_str)

# print(board)
# print(rborad)


print(judge(rboard))