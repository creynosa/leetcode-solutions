import os
import sys

currentDir = os.path.dirname(os.path.realpath(__file__))
relativePath = os.path.join(currentDir, "..")
sys.path.append(relativePath)

import pytest
import twoSum


class TestSolution:
    def test_twoSum(self):
        assert twoSum.Solution.twoSum(self, [0, 4, 3, 0], 0) == [0, 3]
        assert twoSum.Solution.twoSum(self, [0, 0, 0, 0], 0) == [0, 1]
        assert twoSum.Solution.twoSum(self, [-1, -4, -3, 0], -7) == [1, 2]
        assert twoSum.Solution.twoSum(self, [-9, 0, 0, 0], -9) == [0, 1]


if __name__ == "__main__":
    pytest.main()
