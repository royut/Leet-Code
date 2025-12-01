class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        target = sum(nums) % p
        if target == 0:
            return 0
        remainders = {0: -1}
        currSum = 0
        minLen = len(nums)
        for i in range(len(nums)):
            currSum = (currSum + nums[i]) % p
            needed = (currSum - target + p) % p
            if needed in remainders:
                minLen = min(minLen, i - remainders[needed])
            remainders[currSum] = i
        if minLen == len(nums):
            return -1
        return minLen


if __name__ == '__main__':
    print('in main')
    nums = [3, 1, 4, 2]
    p = 6
    # nums = [6, 3, 5, 2]
    # p = 9
    # nums = [1, 2, 3]
    # p = 7
    print(Solution().minSubarray(nums, p))