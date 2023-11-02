class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stair_costs = [0] + cost + [0]
        full_costs = [0] + [1000000] * len(cost) + [1000000]
        for i in range(len(stair_costs)):
            for j in [1, 2]:
                if i + j < len(stair_costs):
                    full_costs[i + j] = min(
                        full_costs[i + j],
                        full_costs[i] + stair_costs[i+j],
                    )
        return full_costs[-1]
