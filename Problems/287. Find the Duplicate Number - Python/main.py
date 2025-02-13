class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


if __name__ == '__main__':
    print("in main")
    print(Solution().findDuplicate([1,3,4,2,2]))
