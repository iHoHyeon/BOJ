N = int(input())
L = []
for _ in range(N):
  L.append(input())

L.sort(key = lambda x : (len(x),x))

for i in range(N):
  if i == N-1:
    print(L[i])
    break

  if L[i] == L[i+1]:
    continue

  print(L[i]) 
