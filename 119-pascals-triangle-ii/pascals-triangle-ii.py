class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row.append(1)
            prev = 1
            for i in range(1, len(row) - 1):
                prev, row[i] = row[i], row[i] + prev
        return row