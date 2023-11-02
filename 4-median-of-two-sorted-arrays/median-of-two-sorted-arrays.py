import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        d, m = divmod(len(nums), 2)
        return nums[d] if m else sum(nums[d-1:d+1]) / 2
