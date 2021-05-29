T = int(input())
for _ in range(T):
  k = int(input())
  n = int(input())

  a = [[]]
  for i in range(n):
    a[0].append(i+1)
  for i in range(k):
    a.append([])
    for j in range(n):
      if j == 0 :
        a[i+1].append(1)  
      else :
        a[i+1].append(a[i+1][j-1]+a[i][j])
  print(a[k][n-1])