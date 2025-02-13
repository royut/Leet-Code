class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)  # rows
        n = len(mat[0])  # columns
        rowsDict = {}
        colsDict = {}
        for i in range(m):
            for j in range(n):
                rowsDict[mat[i][j]] = i
                colsDict[mat[i][j]] = j
        # print(rowsDict)
        # print(colsDict)
        rowFrequency = {}
        colFrequency = {}
        for i in range(m):
            rowFrequency[i] = n
        for i in range(n):
            colFrequency[i] = m
        # print(rowFrequency, colFrequency)
        for i in range(len(arr)):
            row = rowsDict[arr[i]]
            col = colsDict[arr[i]]
            rowFrequency[row] -= 1
            if rowFrequency[row] == 0:
                return i
            colFrequency[col] -= 1
            if colFrequency[col] == 0:
                return i


if __name__ == '__main__':
    print('in main')
    arr = [1, 3, 4, 2]
    mat = [[1, 4], [2, 3]]
    arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
    mat = [[3, 2, 5], [1, 4, 6],[8,7,9]]
    print(Solution().firstCompleteIndex(arr, mat))
