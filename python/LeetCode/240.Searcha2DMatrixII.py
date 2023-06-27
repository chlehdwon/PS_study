"""
Write an efficient algorithm that searches for a target value in an m x
n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""


import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, column = 0, len(matrix[0]) - 1
        while row < len(matrix) and column >= 0:
            if matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
            else:
                return True
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])
        i = bisect.bisect_left([n[-1] for n in matrix], target)
        if i >= row:
            return False
        elif matrix[i][-1] == target:
            return True
        else:
            j = bisect.bisect_left(matrix[-1], target)
            if j >= column:
                return False
            elif matrix[-1][j] == target:
                return True
        for r in range(i, row):
            for c in range(j, column):
                if matrix[r][c] == target:
                    return True
        return False


class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in n for n in matrix)
