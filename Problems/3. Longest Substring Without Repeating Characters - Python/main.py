class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tempSubString = ""
        maxCount = 0
        for char in s:
            if char in tempSubString:
                i = tempSubString.find(char)
                tempSubString = tempSubString[i+1:] + char
            else:
                tempSubString += char
            # print(char, tempSubString)
            if maxCount < len(tempSubString):
                maxCount = len(tempSubString)
        return maxCount


if __name__ == '__main__':
    print('in main')
    print(Solution().lengthOfLongestSubstring("aabaab!bb"))
