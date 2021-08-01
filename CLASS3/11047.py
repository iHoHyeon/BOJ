import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
val = []
for _ in range(N):
    val.append(int(sys.stdin.readline()))
while val:
    temp = K//val[-1]
    if temp > 0:
        K -= val[-1]*temp
        cnt += temp
    val.pop()
print(cnt)
