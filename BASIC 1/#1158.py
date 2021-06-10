N, K = map(int,input().split())
num = [i+1 for i in range(N)]
now = K-1
Y = []
for i in range(N):
  Y.append(str(num.pop(now)))
  if i == N-1 :
    break
  now = (now-1+K)%len(num)

print("<",", ".join(Y),">",sep='')

# join 은 str value를 이용