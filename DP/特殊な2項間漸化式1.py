#・ a_1 = x 
#・ a_n = a_{n-1} + d_1 (n が奇数のとき、n ≧ 3) 
# ・ a_n = a_{n-1} + d_2 (n が偶数のとき)


x,d_1,d_2,k = map(int,input().split())

array = [x] * 1000

for i in range(2,1000):
    if i % 2 == 0:
        array[i] = array[i-1] + d_2
    else:
        array[i] = array[i-1] + d_1

print(array[k])
