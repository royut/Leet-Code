class Solution(object):
    def minMaxSums(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        # print(nums)
        n = len(nums)
        factorial = n
        reverseFactorial = 1
        sumMinMax = sum(nums) * 2
        for i in range(2, k+1):
            # print(i, subArrayCount)
            factorial = factorial * (n - i + 1)
            reverseFactorial = reverseFactorial * i
            subArrayCount = factorial // reverseFactorial
            # print(i, n, n - i, factorial, reverseFactorial)
            print(i, subArrayCount)
            ii = 0
            while subArrayCount > 0:
                print('sub', subArrayCount, k-ii)
                if subArrayCount >= k - ii:
                    print('k-ii;',k-ii, nums[ii],nums[-ii-1])
                    sumMinMax += (k - ii) * nums[ii]
                    sumMinMax += (k - ii) * nums[-ii-1]
                    subArrayCount -= k - ii
                    ii += 1
                else:
                    print('ii;',ii, nums[ii],nums[-ii-1])
                    sumMinMax += ii * nums[ii]
                    sumMinMax += ii * nums[-ii-1]
                    subArrayCount -= ii
                    ii += 1
        return sumMinMax


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3]
    nums = [5, 0, 6]
    nums = [1, 1, 1]
    nums = [2, 2, 2, 3]
    print(Solution().minMaxSums(nums, 4))
