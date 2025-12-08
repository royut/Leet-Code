class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


if __name__ == '__main__':
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
