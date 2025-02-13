class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        currentSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currentSum += nums[i]
            else:
                currentSum = nums[i]
            # print(currentSum)
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum


if __name__ == '__main__':
    print('in main')
    nums = [10, 20, 30, 5, 10, 50]
    nums = [10, 20, 30, 40, 50]
    nums = [12, 17, 15, 13, 10, 11, 12]
    print(Solution().maxAscendingSum(nums))