class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        countTen = 0
        while n > 0:
            r = n % 10
            if r != 0:
                arr.insert(0, r * (10 ** countTen))
            countTen += 1
            n = n // 10
        return arr


if __name__ == "__main__":
    n = 537
    print(Solution().decimalRepresentation(n))