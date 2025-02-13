class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        letters = []
        for i in range(numRows):
            letters.append([])

        direction = 1
        row = 0
        for char in s:
            letters[row].append(char)
            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1
            row += direction

        outputString = ""
        for row in letters:
            for char in row:
                outputString += char

        return outputString


if __name__ == '__main__':
    print('in main')
    s = "abc"
    numRows = 1
    print(Solution().convert(s, numRows))
