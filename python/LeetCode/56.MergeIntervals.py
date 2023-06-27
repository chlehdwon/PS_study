"""
Given an array of intervals where intervals[i] = [starti, endi], merge
all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged


class Solution2:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if output[-1][1] < intervals[i][0]:
                output.append(intervals[i])
            elif output[-1][1] < intervals[i][1]:
                output[-1][1] = intervals[i][1]
        return output


a = Solution()
print(a.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
