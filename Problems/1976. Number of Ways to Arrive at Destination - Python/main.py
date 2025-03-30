class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        edges = {}
        paths = {}
        for i in range(n):
            edges[i] = {}
            paths[i] = float('inf')
        paths[0] = 0
        for road in roads:
            edges[road[0]][road[1]] = road[2]
            edges[road[1]][road[0]] = road[2]
        stack = [0]
        minSoFar = float('inf')
        pathsToEnd = 0
        # print(edges)
        while stack:
            current = stack.pop(0)
            neighbors = edges[current]
            # print(current, stack)
            for neighbor in neighbors:
                if neighbor == n-1:
                    if paths[current] + neighbors[neighbor] == minSoFar:
                        pathsToEnd += 1
                        # print('a', current)
                    elif paths[current] + neighbors[neighbor] < minSoFar:
                        minSoFar = paths[current] + neighbors[neighbor]
                        pathsToEnd = 1
                if paths[current] + neighbors[neighbor] <= paths[neighbor]:
                    paths[neighbor] = paths[current] + neighbors[neighbor]
                    if neighbor not in stack:
                        stack.append(neighbor)
        # print(pathsToEnd, minSoFar)
        return pathsToEnd


if __name__ == '__main__':
    print('in main')
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    # n = 2
    # roads = [[1, 0, 10]]
    print(Solution().countPaths(n, roads))
