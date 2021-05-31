N = int(input())
sol = [0]
for i in range(N):
  if N-i + eval('+'.join(str(N-i))) == N :
    sol.append(N-i)
  if i>54:
    break

print(sol[-1]) 

##시간초과에 유의해서 거꾸로 세는 것이 중요