# 指定した配列（リスト）を定義し、それらの要素のうち5以上の数をすべて足し合わせた値を出力してください。
list = [4, 0, 5, -1, 3, 10, 6, -8]

result = 0
for n in list:
    if n > 4:
        result += n
print(result)
