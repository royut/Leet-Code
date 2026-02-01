class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 2
        i = 1
        count = 1
        while i <= n:
            i = (i + 1) * 2 - 1
            count += 1
            # print('i', i)
        return count


if __name__ == "__main__":
    print('in main')
    n = 7
    print(Solution().countMonobit(n))