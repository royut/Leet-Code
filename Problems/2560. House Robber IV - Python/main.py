class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < left:
                left = nums[i]
            if nums[i] > right:
                right = nums[i]
        while left <= right:
            mid = (left + right) // 2
            checkMid = self.checkWithGuess(nums, k, mid)
            if checkMid:
                right = mid - 1
            else:
                left = mid + 1
        # print(left, right, mid)
        return left

    def checkWithGuess(self, nums, k, guess):
        possible = 0
        index = 0
        while index < len(nums):
            if nums[index] <= guess:
                possible += 1
                index += 2
            else:
                index += 1
        return possible >= k


if __name__ == '__main__':
    print('in main')
    nums = [2, 3, 5, 9]
    k = 2
    print(Solution().minCapability(nums, k))
