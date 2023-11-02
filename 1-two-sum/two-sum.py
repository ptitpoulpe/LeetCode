class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indexes = sorted([(num, i)for i, num in enumerate(nums)])
        for e, (num, i) in enumerate(nums_with_indexes):
            for numb, ib in nums_with_indexes[e+1:]:
                s = num + numb
                if s == target:
                    return (i, ib)
                if s > target:
                    continue
        