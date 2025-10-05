class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        atlantic = [[False for _ in range(n)] for _ in range(m)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if j == m-1:
                    atlantic[j][i] = True
                else:
                    if i == n-1:
                        atlantic[j][i] = True
                    elif (heights[j][i] >= heights[j+1][i] and atlantic[j+1][i]) or (heights[j][i] >= heights[j][i+1] and atlantic[j][i+1]):
                        # print(j, i, atlantic[j+1][i], atlantic[j][i+1])
                        atlantic[j][i] = True
                        if heights[j][i] < heights[j][i+1]:
                            atlantic[j][i+1] = True
                        if heights[j][i] < heights[j+1][i]:
                            atlantic[j+1][i] = True
        # print('atlantic')
        # for i in range(m):
        #     print(atlantic[i])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    pacific[j][i] = True
                else:
                    if i == 0:
                        pacific[j][i] = True
                    elif (heights[j][i] >= heights[j-1][i] and pacific[j-1][i]) or (heights[j][i] >= heights[j][i-1] and pacific[j][i-1]):
                        # print(j, i, pacific[j-1][i], pacific[j][i-1])
                        pacific[j][i] = True
                        if heights[j][i] < heights[j][i-1]:
                            pacific[j][i-1] = True
                        if heights[j][i] < heights[j-1][i]:
                            pacific[j-1][i] = True
        print('pacific')
        for i in range(m):
            print(pacific[i])
        both = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    both.append([i, j])
        return both


if __name__ == "__main__":
    print('in main')
    # heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    # heights = [[1]]
    # heights = [[1,2,3],[18,9,4],[7,6,5]]
    heights = [[10,10,10],[10,1,10],[10,10,10]]
    heights = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
    print(Solution().pacificAtlantic(heights))