class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        maxScore = 0
        for i in range(n):
            currentMax = nums[i]
            currentMin = nums[i]
            for j in range(1, n-i):
                currentMax = max(currentMax, nums[i+j])
                currentMin = min(currentMin, nums[i+j])
                # print(nums[i], nums[i+j], currentMax, currentMin)
                tempScore = currentMax - currentMin
                maxScore = max(maxScore, tempScore)
        # print(maxScore)
        return maxScore * k


if __name__ == "__main__":
    print('in main')
    # nums = [1, 3, 2]
    # k = 2
    nums = [4,2,5,1]
    k = 3
    print(Solution().maxTotalValue(nums, k))