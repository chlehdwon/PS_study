"""
A tree is an undirected graph in which any two vertices are connected
by exactly one path. In other words, any connected graph without simple
cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1
edges where edges[i] = [ai, bi] indicates that there is an undirected
edge between the two nodes ai and bi in the tree, you can choose any
node of the tree as the root. When you select a node x as the root, the
result tree has height h. Among all possible rooted trees, those with
minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer
in any order.

The height of a rooted tree is the number of edges on the longest
downward path between the root and a leaf.
"""


from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # construct bi-directional graph
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # add first leaf nodes
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # delete iteratively until only root nodes remain.
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


class Solution2:
    # My answer. It is very slow... so time limit exceeded occured
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node):
            seen.add(node)
            if graph[node]:
                height = 1
                for u in graph[node]:
                    if u not in seen:
                        height = max(height, dfs(u))
                return height
            return 0

        graph, dict_height = collections.defaultdict(list), \
            collections.defaultdict(list)
        seen = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        for i in list(graph):
            seen = set()
            dict_height[dfs(i)].append(i)
        return dict_height[min(dict_height)]
