class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsDict = {}
        maxNum = float('-inf')
        for num in nums:
            if num > 0 and num not in numsDict:
                numsDict[num] = True
            if num > maxNum:
                maxNum = num
        if len(numsDict) == 0:
            return maxNum
        return sum(numsDict.keys())


if __name__ == '__main__':
    print('in main')
    nums = [-100]
    print(Solution().maxSum(nums))