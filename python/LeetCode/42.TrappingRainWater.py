"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # Move pointer to more higher point
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


class Solution2:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # if we meet the inflection point
            while stack and height[i] > height[stack[-1]]:
                # pop it from the stack
                top = stack.pop()

                if not len(stack):
                    break

                # add the volume of water which is the difference with previous
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume
