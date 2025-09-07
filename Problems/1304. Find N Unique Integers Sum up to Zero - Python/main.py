class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(1, (n // 2) + 1):
            arr.append(i)
            arr.append(-i)
        if n % 2 != 0:
            arr.append(0)
        return arr


if __name__ == "__main__":
    print('in main')
    n = 5
    print(Solution().sumZero(n))