class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        onesCount = 0
        operationFlag = False
        for i in range(len(s)):
            if s[i] == '1':
                onesCount += 1
                if not operationFlag:
                    operationFlag = True
            if s[i] == '0' and operationFlag:
                operationFlag = False
                total += onesCount
            # print(s[i], total)
        return total


if __name__ == '__main__':
    print('in main')
    s = "1001101"
    s = "00111"
    print(Solution().maxOperations(s))