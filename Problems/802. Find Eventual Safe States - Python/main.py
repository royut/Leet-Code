class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        visited = set()
        safe = set()
        n = len(graph)
        for i, row in enumerate(graph):
            if not row:
                safe.add(i)
                visited.add(i)

        def dfs(i):
            visited.add(i)
            print('in function', i)
            for v in graph[i]:
                print(v)
                if v not in visited:
                    dfs(v)
                if v not in safe:
                    return
            safe.add(i)

        for i in range(n):
            if i not in visited:
                dfs(i)

        return sorted(list(safe))


if __name__ == '__main__':
    print('in main')
    graph = [[1, 2], [2, 3], [5], [0], [5], [6], []]
    print(Solution().eventualSafeNodes(graph))