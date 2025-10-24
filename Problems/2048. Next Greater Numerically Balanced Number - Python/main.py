class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n+1, 1224445):
            count = {}
            for dStr in str(i):
                d = int(dStr)
                if d not in count:
                    count[d] = 1
                else:
                    count[d] += 1
            flag = True
            for d in count:
                if count[d] != d:
                    flag = False
            if flag:
                return i


if __name__ == '__main__':
    print('in main')
    n = 13
    print(Solution().nextBeautifulNumber(n))