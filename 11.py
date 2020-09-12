class Solution:
    def maxArea(self, height):
        # height:List[int]
        # rtype:int
        area_max = len(height) * min(height[0], height[-1])
        left, right = 0, len(height)-1
        while left < right:
            if height[left] > height[right]:
                for j in range(right, 0, -1):
                    if height[j] > height[right]:
                        right = j
            else:
                for k in range(left, len(height)):
                    if height[k] >= height[left]:
                        left = k
            area = (right - left) * min(height[left], height[right])
            print(left, right, area)
            if area > area_max:
                area_max = area
        return area_max


a = Solution()
print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
