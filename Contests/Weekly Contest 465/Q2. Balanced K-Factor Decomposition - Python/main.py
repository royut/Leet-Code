class Solution(object):
    def minDifference(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        start = 1
        for i in range(n):
            if i ** k <= n < (i+1) ** k:
                start = i
        print(start)
        ks = []
        for j in range(k):
            for i in range(n):
                if i ** (k-len(ks)) <= n < (i + 1) ** (k-len(ks)):
                    start = i
                    break
            print(ks, n, start, k-len(ks))
            if k-len(ks) > 1:
                for i in range(start, 0, -1):
                    if n % i == 0:
                        ks.append(i)
                        n = n // i
                        break
            else:
                ks.append(n)
        return ks


if __name__ == "__main__":
    # n = 100
    # k = 2
    # n = 44
    # k = 3
    # n = 360
    # k = 4
    # n = 18
    # k = 5
    n = 68
    k = 3
    print(Solution().minDifference(n, k))