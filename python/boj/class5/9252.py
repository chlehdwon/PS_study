import sys

# DP로 푸는 문제
# 역추적 대신 문자열 자체를 memoization도 가능

a = [""] + list(map(str, sys.stdin.readline().strip()))
b = [""] + list(map(str, sys.stdin.readline().strip()))

mem = [["" for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            mem[i][j] = mem[i-1][j-1] + a[i]
        else:
            if len(mem[i-1][j]) >= len(mem[i][j-1]):
                mem[i][j] = mem[i-1][j]
            else:
                mem[i][j] = mem[i][j-1]

result = mem[-1][-1]
print(len(result), result, sep="\n")

# 더 짧은 방법
"""
a = ' '+input()
b = ' '+input()
al, bl = len(a)-1, len(b)-1

dp = [[0]*(bl+1) for _ in range(al+1)]

for i in range(1,al+1):
    for j in range(1,bl+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
ans = ''
while True:
    if al == 0 or bl == 0:
        break;
    if a[al] == b[bl]:
        ans = a[al]+ans
        al, bl = al-1, bl-1
    else:
        if dp[al-1][bl] > dp[al][bl-1]: al -= 1
        else: bl -= 1

print(dp[-1][-1])
print(ans)
"""