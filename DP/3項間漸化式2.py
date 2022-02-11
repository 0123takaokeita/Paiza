# 整数 Q と Q 個の整数 k_1, k_2, ... , k_Q が与えられます。
# 次のように定められた数列の k_i 項目の値を順に出力してください。
# ちなみに、これはフィボナッチ数列と呼ばれる有名な数列です。
# a_1 = 1 
# a_2 = 1 
# a_n= a_{n-2} + a_{n-1} (n ≧ 3) 

cache = [1] * 41

q = int(input())
for i in range(3,41):
    cache[i] = cache[i-1] + cache[i-2]

for i in range(q):
    index = int(input())
    print(cache[index])

