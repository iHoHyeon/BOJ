import sys

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()[1:-1].split(',')
    if n == 0:
        []

    R, L = 0, 0
    check = True

    for i in p:
        if i == "R":
            check = not check
        elif i == "D":
            if check:
                L += 1
            else:
                R += 1
    if R+L <= n:
        res = x[L:n-R]
        if check == False:
            res = res[::-1]
            sys.stdout.write('['+','.join(res)+']\n')
    else:
        sys.stdout.write('error\n')
