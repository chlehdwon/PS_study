import sys

### 이 문제의 핵심은, 메모리 초과 때문에 dp의 index를 memory로 쓰면 안되고, cost로 써야 한다는 점.
### 해당 cost 이하로 만들 수 있는 최대의 memory를 구한 후, 이를 처음으로 넘는 cost를 출력한다는 마인드로 해야 함.
n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
sum_cost = sum(cost)

dp = [[0] * (sum_cost + 1) for _ in range(n)]

for i in range(n):
    for j in range(sum_cost+1):
        if i==0:
            if cost[i] <= j:
                dp[i][j] = memory[i]
        else:
            if j < cost[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + memory[i])

for target_cost in range(sum_cost+1):
    if dp[n-1][target_cost] >= m:
        print(target_cost)
        break

### 이처럼, dp를 1차원 배열로 설정 후, n개의 item에 대해 하나하나 해보면서 dp를 진행하는 경우도 있음.
# n, m = map(int, input().split())
# aarr = tuple(map(int, input().split()))
# carr = tuple(map(int, input().split()))

# dp = [0] * 10001

# for i in range(n):
#    a = aarr[i]
#    c = carr[i]
#    for j in range(10000, c-1, -1):
#       dp[j] = max(dp[j], dp[j-c] + a)

# for i in range(10001):
#    if dp[i] >= m:
#       print(i)
#       break