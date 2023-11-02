class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        neg = None
        zero = ord("0")
        for c in s:
            if c in "+-":
                if neg is not None:
                    break
                neg = c == "-"
            elif c in "0123456789":
                if neg is None:
                    neg = False
                res = res * 10 + ord(c) - zero
            elif c != " " or neg is not None:
                break
        if neg:
            res = -res
        if res < -2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1
        return res