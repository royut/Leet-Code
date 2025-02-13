class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while len(nums) != len(set(nums)):
            if len(nums) > 3:
                nums = nums[3:]
            else:
                nums = []
            count += 1
        return count


if __name__ == '__main__':
    print('in main')
    nums = [6,7,8,9]
    print(Solution().minimumOperations(nums))