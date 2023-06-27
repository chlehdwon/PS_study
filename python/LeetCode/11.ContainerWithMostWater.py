class Solution:
    def maxArea(self, height):
        # height:List[int]
        # rtype:int
        area_max = (len(height)-1) * min(height[0], height[-1])
        left, right, check = 0, len(height)-1, 0
        while left < right:
            if height[left] > height[right]:
                for j in range(right-1, left, -1):
                    if height[j] > height[right]:
                        right = j
                        area = (right - left) * min(height[left],
                                                    height[right])
                        if area > area_max:
                            area_max = area
                        check = 1
                        break
                if check:
                    check = 0
                    continue
                break
            else:
                for k in range(left+1, right):
                    if height[k] > height[left]:
                        left = k
                        area = (right - left) * min(height[left],
                                                    height[right])
                        if area > area_max:
                            area_max = area
                        check = 1
                        break
                if check:
                    check = 0
                    continue
                break
        return area_max

        def maxArea_2(self, height):
            begin, end = 0, len(height) - 1
            area = 0
            while begin != end:
                if height[begin] < height[end]:
                    t = height[begin]*(end - begin)
                    area = max(area, t)
                    begin += 1
                else:
                    t = (height[end]*(end - begin))
                    area = max(area, t)
                    end -= 1
            return area


a = Solution()
print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
