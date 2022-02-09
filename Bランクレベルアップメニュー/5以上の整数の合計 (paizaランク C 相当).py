# 改行区切りで整数がn個入力されるので、n個の整数のうち、5以上のものをすべて足し合わせた値を出力してください
n = int(input())

result = 0
for i in range(n):
  x = int(input())
  if x > 4:
    result += x

print(result)