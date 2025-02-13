class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
