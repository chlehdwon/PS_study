"""
There are n cities connected by m flights. Each flight starts
from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src
and the destination dst,your task is to find the cheapest price
from src to dst with up to k stops. If there is no such route, output -1.
"""

from typing import List
import heapq
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        q = [(0, src, K)]
        for u, v, w in flights:
            graph[u].append((v, w))
        while q:
            w, v, k = heapq.heappop(q)
            if v == dst:
                return w
            if k >= 0:
                for city, price in graph[v]:
                    heapq.heappush(q, (price+w, city, k-1))
        return -1


a = Solution()
print(a.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
