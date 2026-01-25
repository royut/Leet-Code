class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = nums[-1]
        index = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= prev:
                index = i
                break
            prev = nums[i]
        return index+1


if __name__ == "__main__":
    print('in main')
    nums = [1, -1, 2, 3, 3, 4, 5]
    nums = [1, 2, 3, 4]
    nums = [4, 3, -2, -5]
    print(Solution().minimumPrefixLength(nums))