class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_index = len(s) - 1
        t_index = len(t) - 1
        s_to_pass = 0
        t_to_pass = 0
        while True:
            if s_index >= 0:
                if s[s_index] == "#":
                    s_to_pass += 1
                    s_index -= 1
                    continue
                if s_to_pass > 0:
                    s_to_pass -= 1
                    s_index -= 1
                    continue
            if t_index >= 0:
                if t[t_index] == "#":
                    t_to_pass += 1
                    t_index -= 1
                    continue
                if t_to_pass > 0:
                    t_to_pass -= 1
                    t_index -= 1
                    continue
            if s_index < 0 or t_index < 0:
                break
            if s[s_index] != t[t_index]:
                return False
            s_index -= 1
            t_index -= 1
        return s_index == -1 and t_index == -1