from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        return sum(
            comb(v, 2)
            for v in counter.values()
        )
