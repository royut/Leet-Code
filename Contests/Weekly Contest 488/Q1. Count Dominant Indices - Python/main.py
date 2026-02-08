class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumTotal = sum(nums)
        n = len(nums)
        countDom = 0
        for i in range(len(nums)-1):
            sumTotal -= nums[i]
            n -= 1
            if nums[i] > sumTotal / n:
                countDom += 1
        return countDom


if __name__ == "__main__":
    print('in main')
    nums = [4, 1, 2]
    print(Solution().dominantIndices(nums))