N,M = map(int,input().split())
L = list(map(int,input().split()))

B = 0
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if B < L[i]+L[j]+L[k] <= M:
        B = L[i]+L[j]+L[k]
print(B) 
