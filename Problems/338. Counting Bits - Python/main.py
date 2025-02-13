class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            a = [0, 1]
            for i in range(2, n + 1):
                if i % 2 == 0:
                    a.append(a[int(i / 2)])
                else:
                    a.append(a[int((i - 1) / 2)] + 1)
            return a


if __name__ == '__main__':
    print(Solution().countBits(16))
    print (int(11.5))