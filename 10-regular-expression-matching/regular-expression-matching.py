class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Compress p
        np = []
        pi = 0
        while pi < len(p):
            if p[pi] == "*" and pi + 2 < len(p) and p[pi+1] == p[pi-1] and p[pi+2] == "*":
                pi += 1
            else:
                np.append(p[pi])
            pi += 1
        p = "".join(np)

        def match(si=0, pi=0):
            while si < len(s) and pi < len(p):
                if pi+1 < len(p) and p[pi+1] == "*":
                    pi += 1
                #print(si, pi, s[si], p[pi], p[pi-1])
                if p[pi] == "*":
                    if match(si, pi + 1):
                        return True
                    elif s[si] == p[pi-1] or p[pi-1] == ".":
                        si += 1
                    else:
                        pi += 1
                elif s[si] == p[pi] or p[pi] == ".":
                    si += 1
                    pi += 1
                else:
                    return False
            #print(si, pi)
            if pi < len(p) and p[pi] == "*":
                pi += 1
            while pi + 1 < len(p) and p[pi+1] == "*":
                pi += 2
            #print(si, pi)
            return si >= len(s) and pi >= len(p)
        return match()
            