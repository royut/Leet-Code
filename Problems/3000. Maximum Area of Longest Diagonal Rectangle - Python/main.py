from math import sqrt


class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = 0
        max_area = 0
        for i in range(len(dimensions)):
            diag = sqrt(pow(dimensions[i][0], 2) + pow(dimensions[i][1],2))
            if diag > max_diag:
                max_diag = diag
                max_area = dimensions[i][0] * dimensions[i][1]
            elif diag == max_diag and dimensions[i][0] * dimensions[i][1] > max_area:
                max_diag = diag
                max_area = dimensions[i][0] * dimensions[i][1]
        return max_area


if __name__ == "__main__":
    print("in main")
    dimensions = [[9, 3], [8, 6]]
    print(Solution().areaOfMaxDiagonal(dimensions))
