class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        maxNum = nums[0]
        minNum = nums[0]
        for i in range(n):
            if nums[i] > maxNum:
                maxNum = nums[i]
            if nums[i] < minNum:
                minNum = nums[i]
        # print(maxScore)
        return (maxNum - minNum) * k


if __name__ == '__main__':
    print('in main')
    nums = [1, 3, 2]
    k = 2
    print(Solution().maxTotalValue(nums, k))