'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

给定两个非负整数num1和num2表示为string，返回num1和num2的和。

注意：

num1和num2的长度都小于5100。
num1和num2只包含数字0-9。
num1和num2都不包含任何前导零。
您不能使用任何内置的BigInteger库或直接将输入转换为整数。

'''

# -------------------------------------------------------------------------------------------------
# 
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return (ord(num1)+ord(num2)-96)
        
    

S = Solution()
print(S.addStrings("32","0"))

      
# -------------------------------------------------------------------------------------------------



# ------------------------------------------草稿---------------------------------------------------

# -------------------------------------------------------------------------------------------------




# --------------------------------------Best Result------------------------------------------------

# -------------------------------------------------------------------------------------------------

