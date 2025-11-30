class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        preSum = [0, nums[0]]
        for i in range(1, len(nums)):
            preSum.append(preSum[-1] + nums[i])
        # print(nums)
        # print(preSum)
        remainder = preSum[-1] % p
        if remainder == 0:
            return 0
        for i in range(1, len(preSum)-1):
            for j in range(len(preSum) - i):
                # print(j, j+i, nums[j:j+i], preSum[j+i], preSum[j])
                if (preSum[j+i] - preSum[j]) % p == remainder:
                    return i
        return -1


if __name__ == '__main__':
    print('in main')
    nums = [3, 1, 4, 2]
    p = 6
    nums = [6, 3, 5, 2]
    p = 9
    nums = [1, 2, 3]
    p = 7
    print(Solution().minSubarray(nums, p))