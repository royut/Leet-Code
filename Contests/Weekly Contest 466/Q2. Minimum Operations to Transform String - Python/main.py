class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphbet = "abcdefghijklmnopqrstuvwxyz"
        op = 0
        for c in s:
            temp = 26 - alphbet.index(c)
            if temp == 26:
                temp = 0
            if temp > op:
                op = temp
        return op


if __name__ == "__main__":
    print("in main")
    s = "yz"
    # s = "a"
    print(Solution().minOperations(s))