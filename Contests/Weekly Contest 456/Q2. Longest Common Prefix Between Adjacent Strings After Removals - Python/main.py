class Solution(object):
    def longestCommonPrefix(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        lcpaap = []  # longest common prefix among adjacent pairs before modification
        for i in range(len(words)):
            tempMax = 0
            for j in range(len(words)):
                if j == i:
                    continue
                right = j+1
                if right == i:
                    right += 1
                left = j-1
                if left == i:
                    left -= 1
                rightLen = 0
                leftLen = 0
                if right < len(words) and words[right] == words[j]:
                    rightLen = len(words[right])
                if left >= 0 and words[left] == words[j]:
                    leftLen = len(words[left])
                # print(i, j, leftLen, rightLen)
                if max(leftLen, rightLen) > tempMax:
                    tempMax = max(leftLen, rightLen)
            lcpaap.append(tempMax)
        return lcpaap


if __name__ == "__main__":
    print('in main')
    words = ["jump", "run", "run", "jump", "run"]
    words = ["dog", "racer", "car"]
    print(Solution().longestCommonPrefix(words))