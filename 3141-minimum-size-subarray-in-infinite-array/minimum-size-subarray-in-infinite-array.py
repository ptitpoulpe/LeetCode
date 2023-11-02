class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        left = 0
        right = 0
        current = 0
        n = target // sum(nums) * len(nums)
        target = target % sum(nums)
        
        def index(i):
            return i % len(nums)
        
        res = []
        done = set()
        while True:  
            if current < target:
                current += nums[index(right)]
                right += 1
                n += 1
            else:
                if current == target:
                    res.append(n)
                current -= nums[index(left)]
                left += 1
                n -= 1
            sig = (index(left), index(right), right-left)
            if sig in done:
                break
            else:
                done.add(sig)
        return min(res) if res else -1