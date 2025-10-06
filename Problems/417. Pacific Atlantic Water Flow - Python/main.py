class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        atlantic = [[False for _ in range(n)] for _ in range(m)]
        atlanticVisited = [[False for _ in range(n)] for _ in range(m)]
        atlanticStack = [[m-1, i] for i in range(n)]
        atlanticStack.extend([[i, n-1] for i in range(m)])
        while len(atlanticStack) > 0:
            curr = atlanticStack.pop()
            atlanticVisited[curr[0]][curr[1]] = True
            atlantic[curr[0]][curr[1]] = True
            if curr[1] > 0 and heights[curr[0]][curr[1]] <= heights[curr[0]][curr[1]-1] and not atlanticVisited[curr[0]][curr[1]-1]:
                atlanticStack.append([curr[0], curr[1]-1])
            if curr[0] > 0 and heights[curr[0]][curr[1]] <= heights[curr[0]-1][curr[1]] and not atlanticVisited[curr[0]-1][curr[1]]:
                atlanticStack.append([curr[0]-1, curr[1]])
            if curr[1] < n-1 and heights[curr[0]][curr[1]] <= heights[curr[0]][curr[1]+1] and not atlanticVisited[curr[0]][curr[1]+1]:
                atlanticStack.append([curr[0], curr[1]+1])
            if curr[0] < m-1 and heights[curr[0]][curr[1]] <= heights[curr[0]+1][curr[1]] and not atlanticVisited[curr[0]+1][curr[1]]:
                atlanticStack.append([curr[0]+1, curr[1]])
        # print('atlantic')
        # for i in range(m):
        #     print(atlantic[i])

        pacific = [[False for _ in range(n)] for _ in range(m)]
        pacificVisited = [[False for _ in range(n)] for _ in range(m)]
        pacificStack = [[0, i] for i in range(n)]
        pacificStack.extend([[i, 0] for i in range(m)])
        while len(pacificStack) > 0:
            curr = pacificStack.pop()
            pacificVisited[curr[0]][curr[1]] = True
            pacific[curr[0]][curr[1]] = True
            if curr[1] > 0 and heights[curr[0]][curr[1]] <= heights[curr[0]][curr[1]-1] and not pacificVisited[curr[0]][curr[1]-1]:
                pacificStack.append([curr[0], curr[1]-1])
            if curr[0] > 0 and heights[curr[0]][curr[1]] <= heights[curr[0]-1][curr[1]] and not pacificVisited[curr[0]-1][curr[1]]:
                pacificStack.append([curr[0]-1, curr[1]])
            if curr[1] < n-1 and heights[curr[0]][curr[1]] <= heights[curr[0]][curr[1]+1] and not pacificVisited[curr[0]][curr[1]+1]:
                pacificStack.append([curr[0], curr[1]+1])
            if curr[0] < m-1 and heights[curr[0]][curr[1]] <= heights[curr[0]+1][curr[1]] and not pacificVisited[curr[0]+1][curr[1]]:
                pacificStack.append([curr[0]+1, curr[1]])
        # print('pacific')
        # for i in range(m):
        #     print(pacific[i])
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