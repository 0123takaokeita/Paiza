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

# 盤面準備
board = []
for i in range(5):
  board.append(input())


# 縦判定追加
for i in range(5):
  h_str = ''
  for j in range(5):
    h_str += board[j][i]
  board.append(h_str)

# 斜め判定追加
r_str = ''
x_str = ''
for j in range(5):
  # print(j,j)
  r_str += board[j][j]
  x_str += board[j][-1-j]
board.append(r_str)
board.append(x_str)




print(judge(board))