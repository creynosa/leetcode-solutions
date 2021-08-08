# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        numMoves = 0
        for node in (root.left, root.right):
            if node:
                if node.left is None and node.right is None:
                    coinsRequiredChild = 1 - node.val
                    numMoves += abs(coinsRequiredChild)

                    node.val = coinsRequiredChild
                else:
                    numMoves += self.distributeCoins(node)

        childNodeValues = [
            root.val for root in (root.left, root.right) if root is not None
        ]
        coinsRequiredChildren = sum(childNodeValues)
        coinsRequiredParent = 1 - (root.val - coinsRequiredChildren)
        numMoves += abs(coinsRequiredParent)

        root.val = coinsRequiredParent

        return numMoves
