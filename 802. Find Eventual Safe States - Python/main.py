from collections import deque


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        visited = set()
        print(visited)
        n = len(graph)
        nodes = set(range(len(graph)))
        queue = [0]
        cycles = []
        while len(visited) != n:
            print(queue, visited, nodes)
            node = queue.pop(0)
            edges = graph[node]
            visited.add(node)
            nodes.remove(node)
            for edge in edges:
                if edge not in visited:
                    if edge not in queue:
                        queue.append(edge)
                else:
                    cycles.append((edge, node))
            if len(queue) == 0:
                n = nodes.pop()
                nodes.add(n)
                print(n)
                queue.append(n)
                # for i in range(n):
        print('cycles', cycles)


if __name__ == '__main__':
    print('in main')
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print(Solution().eventualSafeNodes(graph))