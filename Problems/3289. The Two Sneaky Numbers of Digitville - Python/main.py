class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsDict = {}
        extras = []
        for i in range(len(nums)):
            if nums[i] in numsDict:
                extras.append(nums[i])
            else:
                numsDict[nums[i]] = 1
        return extras


if __name__ == '__main__':
    print('in main')
    nums = [0, 1, 1, 0]
    print(Solution().getSneakyNumbers(nums))