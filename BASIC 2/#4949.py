while True:
  A = 0 
  B = 0
  check = 0
  now = []
  L = list(input())

  if L == ['.'] : break
  
  for i in L:
    if i == '(':
      A +=1
      now.append(0)
    elif i == ')':
      A += -1
      if(now ==[]) or (now.pop() == 1) :
        check = 1
        break
    elif i == '[':
      B += 1
      now.append(1)
    elif i == ']':
      B += -1
      if (now ==[]) or (now.pop() == 0):
        check = 1
        break
    
    if (A<0)or(B<0) :
      check = 1
      break
  
  if ((A,B) == (0,0)) and check == 0 :
    print("yes")
  else : print("no")
