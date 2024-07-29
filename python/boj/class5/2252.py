import sys
from collections import defaultdict

# topological sort를 통해 풀 수 있음!
# degree가 0인 애들을 queue에 push -> push하는 node와 연결된 edge 제거 -> 이하 반복
# Time complextiy: O(M + N)
m, n = map(int, sys.stdin.readline().split())
in_degree, vertex = [0 for _ in range(m)], defaultdict(list)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    in_degree[b-1] += 1
    vertex[a-1].append(b-1)

queue, line = [], []

for i in range(m):
    if in_degree[i] == 0:
        queue.append(i)
        in_degree[i] = -1

while queue:
    a = queue.pop(0)
    line.append(str(a+1))
    for v in vertex[a]:
        in_degree[v] -= 1
    for i in range(m):
        if in_degree[i] == 0:
            queue.append(i)
            in_degree[i] = -1
        
print(" ".join(line))

### list 대신 deque로 하면 더 빠름
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        print(now, end= " ")

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


topology_sort()
"""