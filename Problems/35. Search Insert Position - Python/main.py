class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # print(left, right, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid + 1
            elif target < nums[mid]:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == '__main__':
    print('in main')
    nums = [1, 3, 5, 6]
    target = 1
    nums = [1, 3]
    target = 0
    print(Solution().searchInsert(nums, target))