# import string

x,y = map(int,input().split(' '))
str = input()

# intab = str[x-1:y]
# outtab = str[x-1:y].upper()
# rule = string.maketrans(intab,outtab)

# str.translate(rule)

result = ''
for i in range(len(str)):
    if i >= x-1 and i <= y-1:
      result += str[i].upper()
    else :
      result += str[i]

print(result)