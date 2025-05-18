class Solution(object):
    def sumOfDigits(self, n):
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        return s

    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        swaps = 0
        for i in range(len(nums)):
            smallestIndex = i
            smallestValue = nums[i]
            for j in range(i, len(nums)):
                if self.sumOfDigits(nums[j]) < self.sumOfDigits(smallestValue):
                    smallestIndex = j
                    smallestValue = nums[j]
                elif self.sumOfDigits(nums[j]) == self.sumOfDigits(smallestValue):
                    if nums[j] < smallestValue:
                        smallestIndex = j
                        smallestValue = nums[j]
            if smallestIndex != i:
                temp = nums[i]
                nums[i] = nums[smallestIndex]
                nums[smallestIndex] = temp
                swaps += 1
        # print(nums, swaps)
        return swaps


if __name__ == '__main__':
    print('in main')
    nums = [37, 100]
    # nums = [22, 14, 33, 7]
    # nums = [18, 43, 34, 16]
    # nums = [277993448,416038674,616955867,539372283]
    print(Solution().minSwaps(nums))
