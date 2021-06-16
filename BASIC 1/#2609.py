A,B = map(int,input().split())
i=1
while(True):
  if A%i ==0 and B%i==0 :
    G = i
  if i >= A or i>=B:
    break
  i += 1
print(G)
print(int(A*B/G))