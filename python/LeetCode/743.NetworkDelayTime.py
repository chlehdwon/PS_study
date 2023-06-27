"""
You are given a network of n nodes, labeled from 1 to n. You are also
given times, a list of travel times as directed edges times[i] = (ui,
vi, wi), where ui is the source node, vi is the target node, and wi is
the time it takes for a signal to travel from source to target.


We will send a signal from a given node k. Return the time it takes for
all the n nodes to receive the signal. If it is impossible for all the
n nodes to receive the signal, return -1.
"""

import collections
import heapq


class Solution:
    # heap answer
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1


class Solution2:
    # queue answer
    def networkDelayTime(self, times, N, K):
        t = [0] + [float("inf")] * N
        graph, q = collections.defaultdict(list), collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1
