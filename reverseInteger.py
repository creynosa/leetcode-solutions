########## FIRST SOLUTION TO THE REVERSE INTEGER PROBLEM


# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = 1
#         if x < 0:
#             sign = -1
#             x = x * sign

#         digits = [digit for digit in str(x)]
#         digits.reverse()
#         reversedNum = int("".join(digits)) * sign

#         if reversedNum not in range(-(2 ** 31), 2 ** 31):
#             return 0
#         else:
#             return reversedNum


########## SECOND REVISED SOLUTION AFTER ASSUMING 32-BIT SIGNED INTEGERS ONLY AVAILABLE IN ENVIRONMENT


class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 2 ** 31 - 1
        minInt = -1 * 2 ** 31

        reversedNum = 0
        while x != 0:
            lastDigit = x % 10 if x >= 0 else x % -10
            x = int(x / 10)

            if reversedNum > (maxInt // 10):
                return 0
            elif reversedNum == maxInt and lastDigit > 7:
                return 0
            elif reversedNum < (minInt / 10):
                return 0
            elif reversedNum == minInt and lastDigit < -8:
                return 0

            tempNum = reversedNum * 10 + lastDigit
            reversedNum = tempNum

        return reversedNum
