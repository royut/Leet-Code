class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        direction = 1 # 1: top and right, 0: bottom and left
        result = []
        i, j = 0, 0
        n, m = len(mat), len(mat[0])
        counted = 0
        while counted < n * m:
            result.append(mat[i][j])
            if direction == 1:
                if j == m-1:
                    direction = 0
                    i += 1
                elif i == 0:
                    direction = 0
                    j += 1
                else:
                    j += 1
                    i -= 1
            elif direction == 0:
                if i == n-1:
                    direction = 1
                    j += 1
                elif j == 0:
                    direction = 1
                    i += 1
                else:
                    j -= 1
                    i += 1
            counted += 1
        return result


if __name__ == "__main__":
    print("in main")
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    mat = [[1, 2], [3, 4]]
    print(Solution().findDiagonalOrder(mat))