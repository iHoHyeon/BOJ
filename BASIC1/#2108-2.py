import sys
from collections import Counter

N = int(input())
L =[]
for _ in range(N):
  L.append(int(sys.stdin.readline()))

S = sorted(L)
print(round(sum(L)/N))
print(S[N//2])

if N == 1:
    print(S[0])
else :
    numS = Counter(S).most_common()
    if numS[0][1] == numS[1][1]:
      print(numS[1][0])
    else :
      print(numS[0][0])
print(S[-1]-S[0])

#Counter를 이용한 최빈값 도출