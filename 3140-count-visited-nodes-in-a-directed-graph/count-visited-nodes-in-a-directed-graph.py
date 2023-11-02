class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        #print("="*10)
        res = [0 for _ in edges]
        def solve(i):
            # there is always a final loop because a node has always a next node
            done = []
            while True:
                if res[i] == -1: # Loop
                    v = len(done) - done.index(i)
                    for j in done[-v:]:
                        res[j] = v
                    for e, j in enumerate(reversed(done[:-v]), 1):
                        res[j] = v + e
                    return
                elif res[i] != 0: # Already computed
                    v = res[i]
                    for e, j in enumerate(reversed(done), 1):
                        res[j] = v + e
                    return
                res[i] = -1
                done.append(i)
                i = edges[i]

        for i in range(len(edges)):
            if res[i] == 0:
                solve(i)
        return res