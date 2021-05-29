import math

A,B,V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))

## 반복문을 이용하면 시간초과##