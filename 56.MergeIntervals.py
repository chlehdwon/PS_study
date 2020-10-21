# Given a collection of intervals, merge all overlapping intervals.


class Solution:
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
