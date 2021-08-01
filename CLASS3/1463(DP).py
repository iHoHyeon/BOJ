# dp[N] = min(dp[N//2],dp[N//3],dp[N-1]) +1


import sys
N = int(sys.stdin.readline())
dp = [0, 0, 1, 1]

for i in range(4, N+1):
    dp.append(dp[i-1]+1)  # case : -1

    if i % 2 == 0:  # case : /2
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])
