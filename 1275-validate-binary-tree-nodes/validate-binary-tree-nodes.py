class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ancestors = [None] * n
        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    if child == i:
                        return False
                    if ancestors[child] is not None:
                        return False
                    if ancestors[i] is None:
                        ancestors[child] = frozenset([i])
                    elif child in ancestors[i]:
                        return False
                    else:
                        ancestors[child] = ancestors[i] | frozenset([i])
        return ancestors.count(None) == 1