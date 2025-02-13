class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sums.append(sum)
            if i == k - 1:
                maxSum = sum
            elif i > k - 1:
                if sum - sums[i - k] > maxSum:
                    maxSum = sum - sums[i - k]
        return float(maxSum) / float(k)


if __name__ == '__main__':
    print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))