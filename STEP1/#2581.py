import math

def pt(a):
  for i in range(1,math.floor(math.sqrt(a))+1):
    if i == 1:
      continue
    if a%i == 0 :
      return 1
  return 0

M = int(input())
N = int(input())
P =[]
if M==1 : M = 2
for i in range(M,N+1):
  if pt(i) == 0:
    P.append(i)

if len(P) == 0:
  print(-1)
else :
  print(sum(P))
  print(min(i for i in P)) 