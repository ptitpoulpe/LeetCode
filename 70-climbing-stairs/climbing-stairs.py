
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        cache_2 = 1
        cache_1 = 1
        cache_0 = None
        for i in range(2, n + 1):
            cache_0 = cache_2 + cache_1
            cache_2 = cache_1
            cache_1 = cache_0

        return cache_0
        
        