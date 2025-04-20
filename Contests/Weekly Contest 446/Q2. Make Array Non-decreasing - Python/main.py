class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = nums[0]
        anomalies = 0
        for i in range(1, len(nums)):
            if nums[i] < maxSoFar:
                anomalies += 1
            else:
                maxSoFar = nums[i]
        return len(nums)-anomalies


if __name__ == '__main__':
    print('in main')
    # nums = [4, 2, 5, 3, 5]
    # nums = [1, 2, 3]
    nums = [19, 80, 63, 74]
    print(Solution().maximumPossibleSize(nums))