class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        flagOne = False
        countingOnes = 0
        total = 0
        for char in s:
            if char == '1' and not flagOne:
                countingOnes += 1
                flagOne = True
            elif char == '1' and flagOne:
                countingOnes += 1
            elif char == '0' and flagOne:
                temp = (countingOnes * (countingOnes + 1)) // 2
                # print(countingOnes, temp)
                total += temp
                flagOne = False
                countingOnes = 0
        if flagOne:
            temp = (countingOnes * (countingOnes + 1)) // 2
            # print(countingOnes, temp)
            total += temp
        return total % 1000000007


if __name__ == '__main__':
    print('in main')
    s = "0110111"
    s = "101"
    s = "111111"
    print(Solution().numSub(s))