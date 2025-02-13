class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        mid = (low + high) // 2
        while True:
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                newMid = (low + mid) // 2
                high = mid
            if target > nums[mid]:
                newMid = (high + mid) // 2
                low = mid
            if newMid == mid:
                return -1
            else:
                mid = newMid


if __name__ == '__main__':
    print('in main')
    print(Solution().search([2,5], 5))
