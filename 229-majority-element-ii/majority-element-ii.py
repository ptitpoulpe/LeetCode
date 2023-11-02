class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        size_by_three = len(nums) // 3
        res = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter.get(num, 0) > size_by_three and num not in res:
                res.append(num)
        return res