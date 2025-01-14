class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        intDict = {}
        countCommons = 0
        commons = []
        for i in range(len(A)):
            # print(A[i], " ", B[i])
            if A[i] not in intDict:
                intDict[A[i]] = 1
            else:
                intDict[A[i]] += 1
                if intDict[A[i]] == 2:
                    countCommons += 1
            if B[i] not in intDict:
                intDict[B[i]] = 1
            else:
                intDict[B[i]] += 1
                if intDict[B[i]] == 2:
                    countCommons += 1
            commons.append(countCommons)
        return commons


if __name__ == '__main__':
    print('in main')
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    A = [2, 3, 1]
    B = [3, 1, 2]
    A = []
    B = []
    print(Solution().findThePrefixCommonArray(A, B))
