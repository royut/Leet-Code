class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        start = 0
        new = []
        if m * n != len(original):
            return []
        for i in range(m):
            nl = original[start: start + n]
            new.append(nl)
            start = start + n
        return new


if __name__ == '__main__':
    print(Solution().construct2DArray([1,2,3,4], 2, 2))