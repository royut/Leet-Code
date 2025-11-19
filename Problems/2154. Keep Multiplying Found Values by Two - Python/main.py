class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == original:
                original *= 2
            elif nums[i] > original:
                break
        return original


if __name__ == '__main__':
    print('in main')
    nums = [5, 3, 6, 1, 12]
    original = 3
    nums = [2, 7, 9]
    original = 4
    print(Solution().findFinalValue(nums, original))