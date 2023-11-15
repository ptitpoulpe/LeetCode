class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_set = set(nums)
        nums = sorted(nums)
        res = 10**6
        best_diff = 10**6
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                diff = target - s
                min_k = 0
                max_k = len(nums) - 1
                while max_k - min_k != 1:
                    mid = min_k + (max_k - min_k) // 2
                    if nums[mid] < diff:
                        min_k = mid
                    else:
                        max_k = mid
                if min_k in (i, j):
                    min_k -= 1
                if max_k in (i, j):
                    max_k += 1

                if min_k >= 0 and (min_k_diff := abs(diff - nums[min_k])) < best_diff:
                    best_diff = min_k_diff
                    res = s + nums[min_k]
                
                if max_k < len(nums) and (max_k_diff := abs(diff - nums[max_k])) < best_diff:
                    best_diff = max_k_diff
                    res = s + nums[max_k]
        return res