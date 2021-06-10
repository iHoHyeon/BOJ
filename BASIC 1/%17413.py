S = list(input())

word = ''
res = ''
tag = 0
for i in S:
  if tag == 0:
    if i == "<":
      word += i
      tag = 1
      continue
    elif i ==' ' :
     word += ' '
     res += word
     word =''
    else : 
      word = i + word
    
  if tag == 1:
    word += i
  
  if i == '>':
    res += word
    word = ''
    tag = 0

print(res+word)
