class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumNums = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            sumNums += sum(nums[start:i+1])
        return sumNums


if __name__ == '__main__':
    print('in main')
    nums = [2,3,1]
    print(Solution().subarraySum(nums))