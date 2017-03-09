'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

给定包含从0,1,2，...，n取得的n个不同数字的数组，找到该数组中缺失的数。

例如，
给定nums = [0，1，3] return 2。

注意：
您的算法应以线性运行时复杂度运行。 你能实现它只使用常量额外的空间复杂性？

积分：
特别感谢@ jianchao.li.fighter添加这个问题和创建所有测试用例。
'''

# -------------------------------------------------------------------------------------------------
# 
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (list((set(range(0,max(nums)+1))) - set(nums))[0]) if (len(nums) != (max(nums)+1)) else (max(nums)+1)



S = Solution()
print(S.missingNumber([0,1]))
print(S.missingNumber([0,1,2,4]))
      
# -------------------------------------------------------------------------------------------------



# ------------------------------------------草稿---------------------------------------------------
# def missingNumber():
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     nums = [0,1,2]
#     nums.sort()
#     return ((list((set(range(0,max(nums)+1))) - set(nums))[0]) if (len(nums) != (max(nums)+1)) else (max(nums)+1))

# print(missingNumber())
# -------------------------------------------------------------------------------------------------




# --------------------------------------Best Result------------------------------------------------
# def missingNumber(self, nums):
#     n = len(nums)
#     return n * (n+1) / 2 - sum(nums)
# -------------------------------------------------------------------------------------------------

# --------------------------------------Best Result------------------------------------------------
'''
Xor-ing with O(1) space

Saw this from ts before. Xoring 0..n results in [n, 1, n+1, 0][n % 4]. 
You can also spot the pattern by looking at xors of such ranges, and it's easy to explain as well.
'''
# def missingNumber(self, nums):
#     n = len(nums)
#     return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]
# -------------------------------------------------------------------------------------------------


# --------------------------------------Best Result------------------------------------------------
# 比较好理解，和-和
# class Solution(object):
#     def missingNumber(self, nums):
#         return sum(range(len(nums)+1)) - sum(nums)
# -------------------------------------------------------------------------------------------------