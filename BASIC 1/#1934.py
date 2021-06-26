def GCD(A,B):
  return GCD(B%A,A) if B%A else A
T = int(input())
for i in range(T):
  A,B = map(int,input().split())
  print(int(A*B/GCD(A,B)))