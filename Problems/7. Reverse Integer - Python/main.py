class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        reversedNum = 0
        negative = False
        if x < 0:
            x = -x
            negative = True
        while x > 0:
            # print(x % 10)
            reversedNum = reversedNum * 10 + (x % 10)
            x = x // 10
        if -pow(2, 31) <= reversedNum <= pow(2, 31)-1:
            if negative:
                return reversedNum * -1
            else:
                return reversedNum
        else:
            return 0


if __name__ == '__main__':
    print('in main')
    print(Solution().reverse(-123))