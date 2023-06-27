"""
Given two arrays, write a function to compute their intersection.
"""

import bisect
from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # Discriminate match or not by using binary search
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # sort both lists
        nums1.sort()
        nums2.sort()
        i = j = 0
        # during moving two pointers to right, decide whether they are same.
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result
