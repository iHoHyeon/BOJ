T = int(input())
score = [0]*301
sum = [0]*301
for i in range(1, T+1):
    score[i] = int(input())
sum[1] = score[1]
sum[2] = score[1]+score[2]
sum[3] = max(score[1]+score[3], score[2]+score[3])

for i in range(4, T+1):
    sum[i] = max(sum[i-3]+score[i-1]+score[i], sum[i-2]+score[i])
print(sum[T])
