class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        alphabetDict = {}
        partitions = []
        for i in range(len(s)):
            foundFlag = False
            for j in range(len(partitions)):
                if s[i] in partitions[j] and not foundFlag:
                    startIndex = j
                    currentStr = partitions[j]
        print(alphabetDict)
        print(partitions)


if __name__ == '__main__':
    print('in main')
    s = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(s))
