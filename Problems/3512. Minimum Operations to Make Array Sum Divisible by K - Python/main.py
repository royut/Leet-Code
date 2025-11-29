class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numsSum = 0
        for i in range(len(nums)):
            numsSum += nums[i]
        return numsSum % k


if __name__ == '__main__':
    print('in main')
    nums = [3, 9, 7]
    k = 5
    print(Solution().minOperations(nums, k))