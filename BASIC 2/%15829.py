L = int(input())
P = list(input())
for i in range(L):
  P[i] = ord(P[i]) - ord('a') + 1

H = 0

for i in range(L):
  H += P[i]*(31**i)
print(H%1234567891)