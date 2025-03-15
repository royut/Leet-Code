class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        notEquals = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                notEquals += 1
                index += 1
        # print(nums)
        return notEquals


if __name__ == '__main__':
    print('in main')
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
