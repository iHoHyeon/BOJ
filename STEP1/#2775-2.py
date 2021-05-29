T = int(input())
for _ in range(T):
  k = int(input())
  n = int(input())

  base = [i for i in range(1,n+1)]

  for _ in range(k):
    for i in range(1,n):
      base[i] += base[i-1]
  print(base[-1])