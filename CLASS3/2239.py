def cal(x, y):
    return (x//3)*3 + (y//3)
def sol(n):
    if n == 81:
        for i in B:
            print(''.join(map(str, i)))
        return True
    x = n // 9
    y = n % 9
    if B[x][y]:
        return sol(n+1)
    else:
        for i in range(1, 10):
            if not R[x][i] and not C[y][i] and not Matrix[cal(x, y)][i]:
                R[x][i] = C[y][i] = Matrix[cal(x, y)][i] = True
                B[x][y] = i
                if sol(n+1):
                    return True
                R[x][i] = C[y][i] = Matrix[cal(x, y)][i] = False
                B[x][y] = 0
    return False
B = [list(map(int, input())) for _ in range(9)]
R = [[False]*10 for _ in range(9)]
C = [[False]*10 for _ in range(9)]
Matrix = [[False]*10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if B[i][j]:
            R[i][B[i][j]] = True
            C[j][B[i][j]] = True
            Matrix[cal(i, j)][B[i][j]] = True
sol(0)
