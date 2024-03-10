import sys

### top-down DP 방식을 사용하여 구현. 
n = int(sys.stdin.readline())

rows, columns = [], []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    rows.append(x)
    columns.append(y)

memory = [[-1] * n for _ in range(n)]

def get_min_multi_cost(start, end):
    if memory[start][end] != -1:
        return memory[start][end]
    elif start >= end:
        memory[start][end] = 0
        return 0
    elif start + 1 == end:
        memory[start][end] = rows[start] * columns[start] * columns[end]
        return rows[start] * columns[start] * columns[end]
    else:
        min_cost = float('inf')
        for mid in range(start, end):
            cost = get_min_multi_cost(start, mid) + get_min_multi_cost(mid+1, end) + rows[start] * columns[mid] * columns[end]
            if cost < min_cost:
                min_cost = cost
        memory[start][end] = min_cost
        return min_cost
            
print(get_min_multi_cost(0, n-1))

### bottom-up의 방식. 이게 속도상으로는 더 빠른듯
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize

# N = int(input())
# m = [[0]*(N+1) for _ in range(N+1)]

# p = []
# a,b = map(int,input().split())
# p.append(a)
# p.append(b)
# for i in range(1, N):
#     a,b = map(int,input().split())
#     p.append(b)

# for i in range(1,N+1):
#     m[i][i] = 0 # 초깃값 셋팅 (i=j인 경우들)

# for i in range(1, N+1) :
#     for j in range(i-1, 0,-1) :
#         min_value = INF
#         for k in range(j,i) :
#             temp_value = m[j][k]+m[k+1][i]+p[j-1]*p[k]*p[i]
#             if min_value > temp_value :
#                 min_value = temp_value
#         m[j][i]= min_value

# print(m[1][N])
