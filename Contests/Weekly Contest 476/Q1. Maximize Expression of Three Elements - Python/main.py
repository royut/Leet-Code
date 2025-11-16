class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2 = float('-inf'), float('inf')
        min1 = float('inf')
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
            if num < min1:
                min1 = num
            # print(max1, max2, min1)
        return max1 + max2 - min1


if __name__ == '__main__':
    print('in main')
    nums = [-2, 0, 5, -2, 4]
    print(Solution().maximizeExpressionOfThree(nums))