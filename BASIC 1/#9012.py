def VPStest(s):
  L = list(s)
  cnt = 0
  if L[0] == ')' : 
    return 'NO'
  for i in range(len(L)):
    if(L[i] == '('):

      cnt += 1
    else : cnt-=1
    if cnt < 0 : 
      return 'NO'
  if cnt == 0 :
    return 'YES'
  else : return 'NO'

T = int(input())

for _ in range(T):
  print(VPStest(input()))
  
