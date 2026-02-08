class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairFlag = True
        while pairFlag:
            i = 1
            pairFlag = False
            while i < len(nums):
                if nums[i-1] == nums[i]:
                    nums[i-1] += nums[i]
                    nums.pop(i)
                    pairFlag = True
                    i = max(i-2, 0)
                i += 1
        return nums


if __name__ == "__main__":
    print('in main')
    nums = [3, 1, 1, 2]
    nums = [2, 2, 4]
    nums = [3, 7, 5]
    nums = [3, 4, 3, 3]
    nums = [1, 2, 2, 4, 4]
    nums = [2, 1, 1, 2]
    print(Solution().mergeAdjacent(nums))