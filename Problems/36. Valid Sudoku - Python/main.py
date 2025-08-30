class Solution(object):

    def checkArray(self, arr):
        return len(set(arr)) == len(arr)

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] != '.':
                    row.append(board[i][j])
                if board[j][i] != '.':
                    col.append(board[j][i])
            if not self.checkArray(row):
                return False
            if not self.checkArray(col):
                return False

        for i in range(3):
            for j in range(3):
                cell = []
                for k in range(3):
                    for l in range(3):
                        if board[i*3+k][j*3+l] != '.':
                            cell.append(board[i*3+k][j*3+l])
                if not self.checkArray(cell):
                    return False
        return True


if __name__ == "__main__":
    print("in main")
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(board))