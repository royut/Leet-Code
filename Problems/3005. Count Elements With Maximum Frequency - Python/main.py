class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsDict = {}
        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
        count = 0
        maxFreq = 0
        for num in numsDict:
            # print(num, numsDict[num])
            if numsDict[num] > maxFreq:
                maxFreq = numsDict[num]
                count = 1
            elif numsDict[num] == maxFreq:
                count += 1
        return count * maxFreq


if __name__ == "__main__":
    print('in main')
    # nums = [1, 2, 2, 3, 1, 4]
    nums = [1, 2, 3, 4, 5]
    print(Solution().maxFrequencyElements(nums))