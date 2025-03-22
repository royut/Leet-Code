class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        edgesDict = {}
        for i in range(n):
            edgesDict[i] = set()
        for edge in edges:
            edgesDict[edge[0]].add(edge[1])
            edgesDict[edge[1]].add(edge[0])
        # print(edgesDict)
        connectedComponentCount = 0
        components = list(range(n))
        # print(components)
        while components:
            currentComponent = components.pop()
            currentNeighbors = edgesDict[currentComponent]
            connectedComponentFlag = True
            # print(currentComponent, currentNeighbors)
            for neighbor in edgesDict[currentComponent]:
                # print('neighbor', neighbor)
                if neighbor in components:
                    components.remove(neighbor)
                neighborChecker = edgesDict[neighbor]
                if neighborChecker.union({neighbor}) != currentNeighbors.union({currentComponent}):
                    connectedComponentFlag = False
                    break
            if connectedComponentFlag:
                connectedComponentCount += 1
        return connectedComponentCount


if __name__ == '__main__':
    print('in main')
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    print(Solution().countCompleteComponents(n, edges))