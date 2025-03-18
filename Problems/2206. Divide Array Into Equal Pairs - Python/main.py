class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsDict = {}
        for n in nums:
            if n in numsDict:
                numsDict[n] += 1
            else:
                numsDict[n] = 1
        for key in numsDict:
            if numsDict[key] % 2 != 0:
                return False
        return True
