class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        current = 0
        for t in target:
            res.extend(["Push", "Pop"] * (t - current - 1))
            res.append("Push")
            current = t
        return res
