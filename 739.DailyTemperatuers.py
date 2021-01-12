"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return T
        stack, day_list = [0], [0 for i in range(len(T))]
        for i in range(1, len(T)):
            while stack and T[stack[-1]] < T[i]:
                for j in stack:
                    day_list[j] += 1
                stack.pop()
            stack.append(i)
        return day_list