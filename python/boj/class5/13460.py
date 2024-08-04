import sys
from collections import deque

# 빡구현.
# BFS를 통해 하나씩 시도하며 조건에 맞는 경우를 찾는 문제.
#   DFS가 아닌 이유는 i) 최대 깊이가 정해져 있고, ii) 처음으로 성공하는 횟수를 구해야 하기 때문.
# move()를 통해 red와 blue의 다음 위치를 구해줌.
# visited 배열을 통해 red와 blue의 배열이 이전에 있었다면 queue에 추가하지 않음.

n, m = list(map(int, sys.stdin.readline().split()))

# #:0, .:1, O: 2
board = [[] for _ in range(n)]
marker_map = {"#": 0, ".": 1, "R": 1, "B": 1, "O": 2}
red, blue, goal = (0, 0), (0, 0), (0, 0)
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# r: 0, d: 1, l: 2, u: 3
def move(dir, red, blue):
    move_map = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    move = move_map[dir]
    ir, jr = red
    ib, jb = blue
    r_go, b_go = True, True

    while r_go | b_go:
        if r_go:
            nir, njr = ir + move[0], jr + move[1]
        if b_go:
            nib, njb = ib + move[0], jb + move[1]

        if board[nir][njr] == 0:
            nir, njr = ir, jr
            r_go = False
        elif board[nir][njr] == 2:
            r_go = False

        if board[nib][njb] == 0:
            nib, njb = ib, jb
            b_go = False
        elif board[nib][njb] == 2:
            b_go = False

        if (nir, njr) == (nib, njb):
            if board[nir][njr] != 2:
                nir, njr = ir, jr
                nib, njb = ib, jb
            r_go, b_go = False, False

        ir, jr, ib, jb = nir, njr, nib, njb

    return (nir, njr), (nib, njb)

for i in range(n):
    row = sys.stdin.readline().split()[0]
    for j, r in enumerate(row):
        board[i].append(marker_map[r])
        if r == "R":
            red = (i, j)
        elif r == "B":
            blue = (i, j)
        elif r == "O":
            goal = (i, j)

visited[red[0]][red[1]][blue[0]][blue[1]] = True
queue = deque([(1, red, blue)])

while queue:
    depth, red, blue = queue.popleft()
    if depth > 10:
        print("-1")
        exit(0)
    for i in range(4):
        new_red, new_blue = move(i, red, blue)
        if new_red == goal:
            if new_blue == goal:
                continue
            print(depth)
            exit(0)
        elif new_blue == goal:
            continue
        elif not visited[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]]:
            visited[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]] = True
            queue.append((depth+1, new_red, new_blue))
print("-1")