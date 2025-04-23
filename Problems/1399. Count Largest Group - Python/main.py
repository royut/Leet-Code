class Solution(object):
    def sumOfDigits(self, s):
        sumOfDigits = 0
        while s > 0:
            sumOfDigits += s % 10
            s = s // 10
        return sumOfDigits

    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        groups = (n+1) * [0]
        for i in range(1, n+1):
            # print(i, self.sumOfDigits(i))
            groups[self.sumOfDigits(i)] += 1
        # print(groups)
        maxGroup = max(groups)
        return groups.count(maxGroup)


if __name__ == '__main__':
    print('in main')
    print(Solution().countLargestGroup(2))
