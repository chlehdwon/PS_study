"""
Find the kth largest element in an unsorted array. Note that it is the
kth largest element in the sorted order, not the kth distinct element.
"""


import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for n in nums:
            heapq.heappush(q, -n)
        for i in range(k):
            largest = heapq.heappop(q)
        return -largest


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


class Solution4:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Solution5:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
