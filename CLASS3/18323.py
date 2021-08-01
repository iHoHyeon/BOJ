N = int(input())
b = list(map(int, input().split()))
a = []
squ = set()
for i in range(1, N+1):
    a.append(i)
    squ.add(i)
    for j in range(len(b)):
        a.append(b[j]-a[j])
        if a[j+1] in squ or (a[j+1] < 1) or (a[j+1] > N):
            a = []
            squ = set()
            break
        squ.add(a[j+1])
        if j == len(b)-1:
            print(*a)
    if a == []:
        continue
    else:
        break
