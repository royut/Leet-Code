class Solution(object):
    def sumOfDigits(self, n):
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        return s

    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == self.sumOfDigits(nums[i]):
                return i
        return -1


if __name__ == '__main__':
    print('in main')
    nums = [1,2,3]
    print(Solution().smallestIndex(nums))