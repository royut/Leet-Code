from math import sqrt


class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n):
            for j in range(i, n):
                c = sqrt(i**2 + j**2)
                if c <= n and c == int(c):
                    count += 1
                elif c > n:
                    break
        return count * 2


if __name__ == "__main__":
    print('in main')
    n = 10
    print(Solution().countTriples(n))