"""
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you
have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is
it possible for you to finish all courses?
"""


import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if course in seen:
                return False
            seen.add(course)
            for y in graph[course]:
                if not dfs(y):
                    return False
            seen.remove(course)
            return True

        seen = set()
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        for i in list(graph):
            if not dfs(i):
                return False
        return True


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # construct graph
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # if the graph is cyclic, return False
            if i in traced:
                return False
            # if we already visit that node, return True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # after search, remove the node from traced
            traced.remove(i)
            # after serach, add the node to visited
            visited.add(i)

            return True

        # judge the graph is cyclic
        for x in list(graph):
            if not dfs(x):
                return False

        return True
