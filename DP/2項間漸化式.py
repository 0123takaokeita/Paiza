x,d = map(int,input().split())
q = int(input())

# 範囲が1000まであるので値を準備する
init = {}
init[1] = x
for i in range(2,1000+1):
    init[i] = init[i-1] + d

# 入力された数値に対応する値を出力
for i in range(q):
    print(init[int(input())])