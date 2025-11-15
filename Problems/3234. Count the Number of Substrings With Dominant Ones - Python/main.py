class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        onesFromStart = [0]
        zerosFromStart = [0]
        countZeros = 0
        countOnes = 0
        for i in range(len(s)):
            if s[i] == '1':
                countOnes += 1
            else:
                countZeros += 1
            onesFromStart.append(countOnes)
            zerosFromStart.append(countZeros)
        # print(onesFromStart)
        # print(zerosFromStart)
        dominant = 0
        total = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                total += 1
                # print(i, j, s[i:j])
                countOnes = onesFromStart[j] - onesFromStart[i]
                countZeros = zerosFromStart[j] - zerosFromStart[i]
                # print(i, j, s[i:j], countOnes, countZeros)
                if countOnes >= countZeros * countZeros:
                    dominant += 1
        # print(dominant, total)
        return dominant


if __name__ == "__main__":
    print('in main')
    s = "00011"
    # s = "101101"
    print(Solution().numberOfSubstrings(s))