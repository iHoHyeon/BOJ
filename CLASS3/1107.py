import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
D = list(sys.stdin.readline().strip())


def IN(n):
    n = list(str(n))
    for i in n:
        if i in D:
            return 0
    return 1


res = abs(100-N)
for i in range(1000001):
    if IN(i):
        res = min(res, len(str(i)) + abs(i-N))
print(res)


# res = abs(N-100)
# for i in range(1000001):
#     i = str(i)
#     for j in range(len(i)):
#         if i[j] in D:
#             break
#         elif j == len(i)-1:
#             res = min(res, abs(N-int(i)) + len(i))
# print(res)
