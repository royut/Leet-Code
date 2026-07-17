class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumOdd = n * n
        sumEven = n * n + n
        while True:
            if sumEven % sumOdd == 0:
                return sumOdd
            sumEven, sumOdd = sumOdd, sumEven % sumOdd


if __name__ == "__main__":
    print('in main')
    n = 5
    print(Solution().gcdOfOddEvenSums(n))