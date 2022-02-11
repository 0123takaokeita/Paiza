# map関数はイテレータを返すためリストに変換
x,d,k = list(map(int,input().split()))

# 内包表記もイテレータを返すためリストに変換
# print(list(int(i) for i in input().split()))

# 配列だとindexのエラーが出やすい
init_array = []
init_array.append(x)
for i in range(1,k):
    init_array.append(init_array[i-1] + d)

print(init_array[k-1])

# 連想配列
init = {}
init[0] = x
for i in range(1,k):
    init[i] = init[i-1] + d

print(init[k-1])