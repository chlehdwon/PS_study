import sys
from collections import deque

# O(nk)에 해결하는 방법
# 위상정렬 같은 느낌으로, in-degree가 제일 낮은 노드에서 시작하여,
# 순차적으로 queue에 넣어가며 update하는 방식이다. 
# DAG의 형태를 띄고 있기 때문에 각각 부분에서 구한 시간이 최적임을 보장할 수 있다.

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().strip().split(" ")))
    build = [0] + list(map(int, sys.stdin.readline().strip().split(" ")))
    edge = [[0 for _ in range(n+1)] for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    min_time = [0 for _ in range(n+1)]
    for i in range(k):
        src, dst = map(int, sys.stdin.readline().strip().split(" "))
        edge[src][dst] = 1
        degree[dst] += 1
    target = int(sys.stdin.readline().strip())
    
    queue = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            queue.append(i)
            min_time[i] = build[i]
    
    while queue:
        node = queue.popleft()
        for i in range(1, n+1):
            if edge[node][i] == 1:
                degree[i] -= 1
                min_time[i] = max(min_time[i], min_time[node] + build[i])
                if degree[i] == 0:
                    if i == target:
                        break
                    queue.append(i)

    print(min_time[target])

# adjacency matrix 대신 edge에 연결된 node들만 담는 방식으로 가면 시간을 절약할 수 있다.