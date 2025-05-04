class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = sorted(list(str(n)))
        return int(nums[-1]) * int(nums[-2])


if __name__ == '__main__':
    print('in main')
    print(Solution().maxProduct(1321))
