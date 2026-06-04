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
            numsArr = []
            currNum = i
            crrNumCount = 0
            while currNum > 0:
                numsArr.append(currNum % 10)
                currNum = currNum // 10
                crrNumCount += 1
                if crrNumCount == 1 or crrNumCount == 2:
                    continue
                if numsArr[crrNumCount-3] < numsArr[crrNumCount-2] and numsArr[crrNumCount-1] < numsArr[crrNumCount-2]:
                    peaks += 1
                if numsArr[crrNumCount-3] > numsArr[crrNumCount-2] and numsArr[crrNumCount-1] > numsArr[crrNumCount-2]:
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