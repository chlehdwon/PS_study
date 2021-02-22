n = int(input())
candy = [list(input().rstrip()) for _ in range(n)]
dx, dy = [1, 0], [0, 1]
def check(d, i, j):
    x, y = i+dx[d], j+dy[d]
    cnt1 = cnt2 = cnt3 = cnt4 = 1
    if d == 0: # d = 0, swap vertical
        # check horizontal
        for k in range(j+1, n):
            if candy[i][j] != candy[i][k]: break
            cnt1 += 1
        for k in range(j-1, -1, -1):
            if candy[i][j] != candy[i][k]: break
            cnt1 += 1
        for k in range(y+1, n):
            if candy[x][y] != candy[x][k]: break
            cnt2 += 1
        for k in range(y-1, -1, -1):
            if candy[x][y] != candy[x][k]: break
            cnt2 += 1
        # check vertical
        for k in range(i-1, -1, -1):
            if candy[i][j] != candy[k][j]: break
            cnt3 += 1
        for k in range(x+1, n):
            if candy[x][y] != candy[k][y]: break
            cnt4 += 1
    else: # d = 1, swap horizontal
        # check vertical
        for k in range(i+1, n):
            if candy[i][j] != candy[k][j]: break
            cnt1 += 1
        for k in range(i-1, -1, -1):
            if candy[i][j] != candy[k][j]: break
            cnt1 += 1
        for k in range(x+1, n):
            if candy[x][y] != candy[k][y]: break
            cnt2 += 1
        for k in range(x-1, -1, -1):
            if candy[x][y] != candy[k][y]: break
            cnt2 += 1
        # check horizontal
        for k in range(j-1, -1, -1):
            if candy[i][j] != candy[i][k]: break
            cnt3 += 1
        for k in range(y+1, n):
            if candy[x][y] != candy[x][k]: break
            cnt4 += 1
    if candy[i][j] == candy[x][y]:
        cnt3 += cnt4
    return max(cnt1, cnt2, cnt3, cnt4)

ans = 0
for i in range(n):
    for j in range(n):
        for d in range(2):
            x, y = i+dx[d], j+dy[d]
            if x < n and y < n:
                candy[i][j], candy[x][y] = candy[x][y], candy[i][j]
                ans = max(ans, check(d, i, j))
                candy[i][j], candy[x][y] = candy[x][y], candy[i][j]

print(ans)