n = int(input())

result = 0
for i in range(n):
    pair = input().split(' ')
    if pair[0] == pair[1]:
      result += int(pair[0]) * int(pair[1])
    else:
      result += int(pair[0]) + int(pair[1])

print(result)