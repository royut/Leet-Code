class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        opCount = 0
        while index < len(nums) - 3:
            if nums[index] == 0:
                nums[index] = int(not nums[index])
                nums[index + 1] = int(not nums[index + 1])
                nums[index + 2] = int(not nums[index + 2])
                opCount += 1
            index += 1
        if nums[-3:] == [0, 0, 0]:
            return opCount + 1
        if nums[-3:] == [1, 1, 1]:
            return opCount
        return -1


if __name__ == '__main__':
    print('in main')
    nums = [0, 1, 1, 1, 0, 0]
    nums = [1, 1, 1]
    print(Solution().minOperations(nums))