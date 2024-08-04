import sys

# 전형적인 DP
# dp(S, E) = arr[S] == arr[E] and dp(S-1, E-1)
# Top-down으로 풀어서 시간이 조금 더 나왔다.
# Time Complextiy: O(n)

n = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().strip().split(" ")
m = int(sys.stdin.readline().strip())

mem = [[-1 if i != j else 1 for i in range(n)] for j in range(n)]
for i in range(n-1):
    mem[i][i+1] = 1 if arr[i] == arr[i+1] else 0

def dp(s, e):
    if mem[s][e] != -1:
        return mem[s][e]
    else:
        res = int(arr[s] == arr[e] and dp(s+1, e-1))
        mem[s][e] = res
        return res

for _ in range(m):
    s, e = map(int, sys.stdin.readline().strip().split(" "))
    print(dp(s-1, e-1))

# 아래는 Bottom-up 풀이
"""
n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

d = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    d[i][i] = 1

for i in range(n-1):
    if seq[i] == seq[i+1]:
        d[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if seq[j] == seq[j+i] and d[j+1][j+i-1] == 1:
            d[j][j+i] = 1

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(d[s-1][e-1])
"""