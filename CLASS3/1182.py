from itertools import combinations

N, S = map(int, input().split())
num = list(map(int, input().split()))

ans = 0

for len in range(1, N+1):
    temp = list(combinations(num, len))
    for i in temp:
        if sum(i) == S:
            ans += 1


print(ans)
