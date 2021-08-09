import os
import sys

currentDir = os.path.dirname(os.path.realpath(__file__))
relativePath = os.path.join(currentDir, "..")
sys.path.append(relativePath)

import pytest
from distributeCoinsTree import Solution, TreeNode


class DistributeCoinsSolutionTest:
    def test_distributeCoins(self):
        tree = TreeNode[0, 0, 3]
        assert Solution.distributeCoins(self, tree) == 3

        tree = TreeNode[1, 1, 1]
        assert Solution.distributeCoins(self, tree) == 0

        tree = TreeNode[1, TreeNode[0, None, 3], 0]
        assert Solution.distributeCoins(self, tree) == 4

        tree = TreeNode[2, 1, 0]
        assert Solution.distributeCoins(self, tree) == 1

        tree = TreeNode[1, 0, TreeNode[0, None, 3]]
        assert Solution.distributeCoins(self, tree) == 4

        tree = TreeNode[
            0,
            TreeNode[2, None, TreeNode[0, None, TreeNode[0, 1, 1]]],
            TreeNode[0, 2, 3],
        ]
        assert Solution.distributeCoins(self, tree) == 9


if __name__ == "__main__":
    pytest.main()
