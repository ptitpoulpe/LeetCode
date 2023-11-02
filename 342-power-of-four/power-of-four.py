class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n & 0b11 != 0:
                return False
            n = n >> 2
        return True