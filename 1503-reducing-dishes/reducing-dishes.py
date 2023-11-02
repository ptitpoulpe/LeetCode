class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat = reversed(sorted(satisfaction))
        result = 0
        sum_sat = 0
        for s in sat:
            sum_sat += s
            new_result = result + sum_sat
            if new_result < result:
                return result
            result = new_result

        return result

        