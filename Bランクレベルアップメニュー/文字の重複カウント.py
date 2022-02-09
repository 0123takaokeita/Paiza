target = input()
word = input()

count = 0
for i in range(len(word)-(len(target)-1)):
  pair = word[i:i+len(target)]
  if pair == target:
      count += 1

print(count)