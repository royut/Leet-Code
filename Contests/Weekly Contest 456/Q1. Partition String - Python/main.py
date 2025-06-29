class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        partitions = set()
        partitionsList = []
        tempS = ""
        for char in s:
            tempS = tempS + char
            if tempS not in partitions:
                partitions.add(tempS)
                partitionsList.append(tempS)
                tempS = ""
        return partitionsList


if __name__ == '__main__':
    print('in main')
    s = "abbccccd"
    print(Solution().partitionString(s))