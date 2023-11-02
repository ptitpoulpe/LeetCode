class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        neg = False 
        if k == 1: 
            return 0 
        m = k - 1
        while True: 
            pow2 = math.floor(math.log(m, 2)) 
            d, m = divmod(m, 2 ** pow2) 
            if d == 0 or m == 0: 
                break 
            neg = not neg 
        return int(m if neg else not m) 
 