#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        moji = list(str(x))
        i = 0
        while i < (len(moji) / 2):
            if moji[i] == moji[len(moji)-1-i]:
                i = i+1
                continue
            else:
                return False
        return True


# @lc code=end

