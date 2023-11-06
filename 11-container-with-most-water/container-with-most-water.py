class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(l, r):
            return abs(l - r) * min(height[l], height[r])
        left = 0
        right = len(height) - 1
        res = -1
        while left < right:
            new_area = area(left, right)
            if new_area > res:
                res = new_area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res