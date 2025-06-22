class Solution(object):
    def checkPrime(self, num):
        if num < 2:
            return False
        countN = 0
        for i in range(1, num+1):
            if num % i == 0:
                countN += 1
        if countN == 2:
            return True
        else:
            return False

    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsDict = {}
        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
        for num in numsDict:
            if self.checkPrime(numsDict[num]):
                return True
        return False


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3, 4, 5, 4]
    # nums = [1, 2, 3, 4, 5]
    print(Solution().checkPrimeFrequency(nums))