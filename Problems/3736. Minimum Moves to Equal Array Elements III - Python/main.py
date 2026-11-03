class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = max(nums)
        sumVal = 0
        for num in nums:
            sumVal += maxVal - num
        return sumVal