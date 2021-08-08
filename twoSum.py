############# FIRST SOLUTION TO THE TWO SUM PROBLEM

# import itertools

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for combination in itertools.combinations(nums, 2):
#             sumPair = sum(combination)
#             if sumPair == target:
#                 firstNumIdx = nums.index(combination[0])
#                 secondNumIdx = nums.index(combination[1])
#                 if secondNumIdx == firstNumIdx:
#                     secondNumIdx = nums.index(combination[1], (firstNumIdx + 1))
#                 return list([firstNumIdx, secondNumIdx])


############ REVISED SOLUTION


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in table:
                table[num] = i
            else:
                return [table[diff], i]
