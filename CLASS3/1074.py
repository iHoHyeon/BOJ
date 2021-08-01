N, r, c = map(int, input().split())

now = 0

while N > 1:
    N -= 1
    t = 2**N
    if r < t and c < t:
        now += (0)
    elif r < t and c >= t:
        c -= t
        now += (t**2)
    elif r >= t and c < t:
        r -= t
        now += (2*t**2)
    elif r >= t and c >= t:
        r -= t
        c -= t
        now += (3*t**2)

now += (2*r + c)
print(now)
