class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countV = 0
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u']:
                countV += 1
        # print(countV)
        if countV == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    print('in main')
    s = "leetcoder"
    print(Solution().doesAliceWin(s))