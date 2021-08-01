def star3(n):
  global arr
  if n==3:
    arr[0][:3]=arr[2][:3]=[1]*3
    arr[1][:3]=[1,0,1]
    return
  a = int(n/3)
  star3(a)
  for i in range(3):
    for j in range(3):
      if (i,j)==(1,1):
        continue
      for k in range(a):
        arr[i*a+k][j*a:(j+1)*a] =arr[k][:a]


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

star3(N)
for i in range(N):
  for j in range(N):
    print('*'if arr[i][j] else ' ',end = '')
  print()

