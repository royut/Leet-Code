class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = []
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeros.append(0)
            else:
                i += 1
        nums.extend(zeros)


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)
