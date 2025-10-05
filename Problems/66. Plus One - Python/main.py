class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        passing = 1
        while n > 0:
            digits[n-1] += passing
            if digits[n-1] == 10:
                digits[n-1] = 0
                passing = 1
                n -= 1
            else:
                return digits
        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    print('in main')
    digits = [1, 9]
    print(Solution().plusOne(digits))