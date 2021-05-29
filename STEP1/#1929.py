
def pt(a):
  if a == 1:
    return 0
  for i in range(2,int(a**(0.5))+1):
    if a%i == 0 :
      return 0
  return 1

M,N = map(int,input().split())

for i in range(M,N+1):
  if pt(i)== 1 :
    print(i)