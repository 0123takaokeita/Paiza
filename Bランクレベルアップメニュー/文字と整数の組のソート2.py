n = int(input())
dict = {}
# バリューの合計
for i in range(n):
  x,y = input().split()
  if (x in dict):
    dict[x] = dict[x] + int(y)
  else:
    dict[x] = int(y)

# キーバリュー反転
rdict = {}
for i in dict:
  rdict[dict[i]] = i

# ソートして出力
sorted = sorted(dict.values(), reverse=True)
for i in sorted:
  print(f"{rdict[i]} {i}")
