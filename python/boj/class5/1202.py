import sys
import heapq

# Greedy와 우선정렬 queue가 합쳐진 형태
# 우선 가방을 무게 순으로 정렬한 후, 해당 무게보다 가벼운 보석 중 가장 비율이 좋은 보석을 순차적으로 담는 법.
# 해당 구현을 위해 heapq를 사용
N, K = map(int, sys.stdin.readline().strip().split(" "))
M, V, C = [0 for _ in range(N)], [0 for _ in range(N)], [0 for _ in range(K)]

for i in range(N):
    M[i], V[i] = map(int, sys.stdin.readline().strip().split(" "))

for i in range(K):
    C[i] = int(sys.stdin.readline().strip())

C.sort()
ratio = sorted([(M[i], V[i]) for i in range(N)])

max_value, heap = 0, []
for bag in C:
    while ratio and ratio[0][0] <= bag:
        heapq.heappush(heap, -ratio[0][1])
        heapq.heappop(ratio)
    if heap:
        max_value -= heapq.heappop(heap)

print(max_value)

# reverse로 정의한 후, pop을 하면 더 짧게 할 수 있음.
"""
import sys
from heapq import heappop, heappush

n, k = map(int,sys.stdin.readline().rstrip().split())

mass = []
dia = {}
for i in range(n):
    m, v = map(int,sys.stdin.readline().rstrip().split())
    mass.append(m)
    if m in dia:
        dia[m].append(v)
    else:
        dia[m]=[v]
mass.sort()
mass.reverse()

for m in dia:
    dia[m].sort()

bag = []
for i in range(k):
    bag.append(int(sys.stdin.readline().rstrip()))
bag.sort()
bag.reverse()

ans = 0
val = []
while bag:
    w = bag.pop()
    mpop = set()
    while mass and mass[-1]<=w:
        mpop.add(mass.pop())
    for m in mpop:
        for v in dia[m]:
            heappush(val,-v) #최대 힙
    if val:
        ans+=-heappop(val)

print(ans)
"""