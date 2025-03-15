class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        lastNum = nums[0]
        uniques = 1
        while index < len(nums):
            if nums[index] == lastNum:
                nums.pop(index)
            else:
                lastNum = nums[index]
                index += 1
                uniques += 1
        return uniques


if __name__ == '__main__':
    print('in main')
    print(Solution().removeDuplicates([1,1,1,2, 2, 2,2]))
