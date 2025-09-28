class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for i in range(n-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


if __name__ == "__main__":
    nums = [2, 1, 2]
    nums = [1, 2, 1, 10]

    print(Solution().largestPerimeter(nums))