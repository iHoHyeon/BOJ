T = int(input())

for _ in range(T):
    n = int(input())
    H = {}
    for _ in range(n):
        name, wear = map(str, input().split())
        if wear in H:
            H[wear] += 1
        else:
            H[wear] = 1
    cnt = 1
    for i in H.values():  # value들의 list 생성 -> dict.values()
        cnt *= (i+1)
    print(cnt-1 if n > 0 else 0)
