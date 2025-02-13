class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums.exclude(list(set(nums)))


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3, 4]
    nums.remove(1)
    print(nums)
