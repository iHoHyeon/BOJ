import sys
r = 1000000
check = [True for _ in range(r)]

for i in range(2,r//2+1):
  if check[i]==True:
    for j in range(i+i,r,i):
      if check[j] ==True :
        check[j] = False


while(1):
  n = int(sys.stdin.readline())
  if n == 0 : 
    break

  for i in range(3,n):
    if check[i] == True and check[n-i] == True:
      print("%d = %d + %d"%(n,i,n-i))
      break
    elif i > n/2 :
      print("Goldbach's conjecture is worng")
      break

##에라토스테네스의 채로 소수를 구하자