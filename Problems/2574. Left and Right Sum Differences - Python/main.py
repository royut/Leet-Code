class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = 0
        rightSum = 0
        ans = []
        for i in range(len(nums)):
            ans.append(rightSum)
            rightSum += nums[i]
        # print(ans)
        for i in range(len(nums)-1, -1, -1):
            ans[i] -= leftSum
            if ans[i] < 0:
                ans[i] *= -1
            leftSum += nums[i]
        return ans


if __name__ == '__main__':
    print('in main')
    nums = [10, 4, 8, 3]
    print(Solution().leftRightDifference(nums))