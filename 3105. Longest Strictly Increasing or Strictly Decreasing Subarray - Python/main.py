class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countIncreasingNums = 1
        countDecreasingNums = 1
        maxLength = 1
        minLength = 1
        for i in range(1, len(nums)):
            # print(nums[i-1], countIncreasingNums)
            if nums[i] > nums[i-1]:
                countIncreasingNums += 1
            else:
                countIncreasingNums = 1
            if countIncreasingNums > maxLength:
                maxLength = countIncreasingNums
            if nums[i] < nums[i-1]:
                countDecreasingNums += 1
            else:
                countDecreasingNums = 1
            if countDecreasingNums > minLength:
                minLength = countDecreasingNums
        return max(maxLength, minLength)


if __name__ == '__main__':
    print('in main')
    nums = [1, 4, 3, 3, 2]
    # nums = [3, 3, 3, 3]
    # nums = [3, 2, 1]
    print(Solution().longestMonotonicSubarray(nums))
