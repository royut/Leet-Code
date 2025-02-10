class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        while i < len(s) and s != "":
            print(s, i)
            char = s[i]
            if char.isdigit():
                s = s[:max(0, i-1)] + s[i+1:]
                i = max(i-2, 0)
            else:
                i += 1
        return s


if __name__ == '__main__':
    print('in main')
    print('s', Solution().clearDigits("cb34"))