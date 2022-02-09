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

r_str = ''
x_str = ''
for j in range(5):
  # print(j,j)
  r_str += board[j][j]
  x_str += board[j][-1-j]

rboard.append(r_str)
rboard.append(x_str)

# print(board)
# print(rboard)


print(judge(rboard))