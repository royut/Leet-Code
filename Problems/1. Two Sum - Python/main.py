class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)
        f = 0
        l = len(nums_sorted) - 1
        while True:
            if nums_sorted[f] + nums_sorted[l] == target:
                if nums_sorted[f] == nums_sorted[l]:
                    return [nums.index(nums_sorted[f]), nums[nums.index(nums_sorted[f]) + 1:].index(nums_sorted[l]) + len(nums) - len(nums[nums.index(nums_sorted[f]) + 1:])]
                return [nums.index(nums_sorted[f]), nums.index(nums_sorted[l])]
            if nums_sorted[f] + nums_sorted[l] < target:
                f += 1
            if nums_sorted[f] + nums_sorted[l] > target:
                l -= 1


if __name__ == '__main__':
    print("in main")
    print(Solution().twoSum([3,2,3], 6))
