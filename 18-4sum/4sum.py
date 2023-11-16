class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        oneSums = defaultdict(int)
        for num in nums:
            oneSums[num] += 1
        
        oneSumsSorted = sorted(oneSums.items())
        twoSums = defaultdict(list)
        for i in range(len(oneSumsSorted)):
            vi, ci = oneSumsSorted[i]
            for j in range(i, len(oneSumsSorted)):
                vj, cj = oneSumsSorted[j]
                twoSums[vi + vj].append([vi, vj])
        
        twoSumsSorted = sorted(twoSums.items())
        res = set()
        for i in range(len(twoSums)):
            vi, cis = twoSumsSorted[i]
            for j in range(i, len(twoSums)):
                vj, cjs = twoSumsSorted[j]
                if vi + vj > target:
                    break 
                if vi + vj == target:
                    for ci in cis:
                        for cj in cjs:
                            cs = defaultdict(int)
                            for c in ci + cj:
                                cs[c] += 1
                            if all(
                                oneSums[k] >= v
                                for k, v in cs.items()
                            ):
                                res.add(tuple(sorted(ci + cj)))
        return res
