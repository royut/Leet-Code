class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums) // 3
        # print(nums)
        max_sum = 0
        for i in range(n):
            nums.pop()
            max_sum += nums.pop()
        return max_sum


if __name__ == '__main__':
    print('in main')
    nums = [2, 1, 3, 2, 1, 3]
    nums = [1, 1, 10, 10, 10, 10]
    print(Solution().maximumMedianSum(nums))