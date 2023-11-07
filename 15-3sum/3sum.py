class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        values = {}
        for num in nums:
            values[num] = values.get(num, 0) + 1
        
        res = set()
        svalues = sorted(values.items())
        for i in range(len(svalues)):
            vi, ci = svalues[i]
            for j in range(i, len(svalues)):
                vj, cj = svalues[j]
                v = vi + vj
                #print(vi, ci, vj, cj, -v)
                if vi == 0 and vj == 0:
                    if cj >= 3:
                        res.add((0, 0, 0))
                    continue
                if -v < vj or (-v == vj and cj == 1):
                    #print("continue")
                    continue
                if -v > svalues[-1][0]:
                    #print("Continue")
                    continue
                if -v in values and (i != j or ci > 1):
                    #print("added")
                    res.add(tuple(sorted([vi, vj, -v])))
        return res