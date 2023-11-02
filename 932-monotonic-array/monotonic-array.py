class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        first = nums[0]
        last = nums[-1]

        if first < last:
            comparator = lambda x,y : x <= y
        elif first > last:
            comparator = lambda x,y : x >= y
        else:
            comparator = lambda x,y : x == y

        for i in range(len(nums) - 1):
            if not comparator(nums[i], nums[i+1]):
                return False
        
        return True
        