from math import inf
from heapq import heappush, heappop, heapify
import sys

v, e = map(int,sys.stdin.readline().split())
graph = {i: {} for i in range(1,v+1)}
visited = [False] * (v+1)
mst=0   
cnt=0

for _ in range(e):
    u, v, cost = map(int, sys.stdin.readline().split())
    if u!=v:
        graph[u][v]=cost
        graph[v][u]=cost

pq = []
heappush(pq, (0,1))
while len(pq) and cnt<=v:
    min_cost, u = heappop(pq)
    if not visited[u]:
        visited[u]=True
        mst += min_cost
        cnt += 1
        for w, cost in graph[u].items():
                heappush(pq, (cost,w))  

print(mst)