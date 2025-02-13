class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        digits = "0123456789"
        sign = 0
        for char in s:
            if char == " " and sign == 0:
                continue
            t = digits.find(char)
            # print(t, char)
            if t == -1 and char != '-' and char != '+':
                break
            if t != -1:
                if sign == 0:
                    sign = 1
                num = num * 10 + t
            else:
                if char == '-' and sign == 0:
                    sign = -1
                elif char == '+' and sign == 0:
                    sign = 1
                else:
                    break
        if num * sign > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif num * sign < -pow(2, 31):
            return -pow(2, 31)
        return num * sign


if __name__ == '__main__':
    print('in main')
    s = "    -042"
    s = "42"
    s = "1337c0d3"
    s = "0-1"
    s = "words and 987"
    s = "-91283472332"
    print(Solution().myAtoi(s))
