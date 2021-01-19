"""
Given a list of airline tickets represented by pairs of departure and
arrival airports [from, to], reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the
itinerary that has the smallest lexical order when read as a single
string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical
order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
"""


import collections
from typing import List


class Solution:
    # dfs answer
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # organize the reversed graph
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            # visit lexically by passing the first value
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # reverse one more time
        return route[::-1]


class Solution2:
    # iterative with stack
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]
