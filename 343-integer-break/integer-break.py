class Solution:
    def integerBreak(self, n: int) -> int:
        res = 0
        for i in range(1, n):
            d, m = divmod(n, i)
            r1 = i ** d * m
            if r1 > res:
                res = r1
            
            if d > 1:
                r2 = i ** (d - 1) * (m + i)
                if r2 > res:
                    res = r2
             
            #print(f"i:{i}, d:{d}, m:{m}, r1:{r1}, r2:{r2}")

        return res