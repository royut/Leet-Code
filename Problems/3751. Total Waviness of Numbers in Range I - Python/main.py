class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        peaks = 0
        valleys = 0
        for i in range(num1, num2 + 1):
            ppp, pp, p = -1, -1, -1
            currNum = i
            crrNumCount = 0
            while currNum > 0:
                ppp = pp
                pp = p
                p = currNum % 10
                currNum = currNum // 10
                crrNumCount += 1
                if crrNumCount == 1 or crrNumCount == 2:
                    continue
                if ppp < pp and p < pp:
                    peaks += 1
                if ppp > pp and p > pp:
                    valleys += 1
            # print(numsArr, peaks, valleys)
        return peaks + valleys


if __name__ == "__main__":
    print('in main')
    # num1 = 120
    # num2 = 130
    # num1 = 198
    # num2 = 202
    num1 = 4848
    num2 = 4848
    print(Solution().totalWaviness(num1, num2))