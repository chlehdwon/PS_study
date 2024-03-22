import sys
sys.setrecursionlimit(10**7)

distance = [[1, 2, 2, 2, 2],
            [2, 1, 3, 4, 3],
            [2, 3, 1, 3, 4],
            [2, 4, 3, 1, 3],
            [2, 3, 4, 3, 1]]
arr = list(map(int, sys.stdin.readline().split()))
n = len(arr) - 1

memory = [[[-1] * n for _ in range(5)] for _ in range(5)]

def dp(idx, left, right):
    if idx>=n:
        return 0
    elif memory[left][right][idx] != -1:
        return memory[left][right][idx]
    else:
        target = arr[idx]
        left_cost = distance[left][target] + dp(idx+1, target, right)
        right_cost = distance[right][target] + dp(idx+1, left, target)
        memory[left][right][idx] = min(left_cost, right_cost)
        return memory[left][right][idx]

print(dp(0, 0, 0))