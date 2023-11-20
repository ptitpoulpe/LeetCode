class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        open_braces = "([{"
        close_braces = ")]}"
        for c in s:
            if (obi := open_braces.find(c)) != -1:
                queue.append(obi)
            elif len(queue) == 0 or close_braces.find(c) != queue.pop():
                return False
        return len(queue) == 0


                