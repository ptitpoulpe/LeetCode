class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def test(on, cn, done=""):
            if on == 0:
               res.append(done + ")" * cn) 
               return
            if cn > on:
                test(on, cn - 1, done + ")")
            if on > 0:
                test(on - 1, cn, done + "(")
        test(n, n)
        return res