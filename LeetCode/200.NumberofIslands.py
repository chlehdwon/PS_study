"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the
number of islands.

An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid) -> int:
        # by using DFS, turn the value to '0' until there is no adjacent land.
        # we don't have to give gird to parameter
        # because this method is nested function.
        def backtracking(gird, i, j):
            grid[i][j] = '0'
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                backtracking(grid, i, j+1)
            if i < len(grid)-1 and grid[i+1][j] == '1':
                backtracking(grid, i+1, j)
            if j > 0 and grid[i][j-1] == '1':
                backtracking(grid, i, j-1)
            if i > 0 and grid[i-1][j] == '1':
                backtracking(grid, i-1, j)
            return
        island_num = 0
        # during iterating the grid, do backtracking.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    backtracking(grid, i, j)
                    island_num += 1
        return island_num


class Solution2:
    def numIslands(self, grid) -> int:
        # it is improved version of backtracking
        def backtracking(i, j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return
            grid[i][j] = '0'
            backtracking(i+1, j)
            backtracking(i-1, j)
            backtracking(i, j+1)
            backtracking(i, j-1)
            return
        island_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    backtracking(grid, i, j)
                    island_num += 1
        return island_num


a = Solution()
print(a.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
