class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        start = None
        end = None
        possible = set()
        for x, line in enumerate(grid):
            for y, cell in enumerate(line):
                if cell == 1:
                    start = (x, y)
                elif cell == 2:
                    end = (x, y)
                    possible.add(end)
                elif cell == 0:
                    possible.add((x, y))
        
        def solve(current, possible):
            if current == end:
                return 1 if len(possible) == 0 else 0
            cx, cy = current
            res = 0
            for dx, dy in [
                (-1, 0),
                (0, -1),
                (1, 0),
                (0, 1),
            ]:
                new = (cx + dx, cy + dy)
                if new in possible:
                    # quite ugly :)
                    possible.remove(new)
                    res += solve(new, possible)
                    possible.add(new)
            return res
        return solve(start, possible)
        