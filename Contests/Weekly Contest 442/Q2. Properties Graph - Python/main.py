class Solution(object):
    def intersect(self, nums1, nums2):
        nums = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums.add(nums1[i])
        return len(nums)

    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        graph = {}
        for i in range(len(properties)):
            graph[i] = []
        for i in range(len(properties)):
            for j in range(i+1, len(properties)):
                if self.intersect(properties[i], properties[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)
        # print(graph)
        components = list(graph.keys())
        visited = []
        connected = 0
        stack = []
        while components:
            if len(stack) > 0:
                current = stack.pop()
            else:
                connected += 1
                current = components.pop()
            # print(current, stack, visited, components)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    if neighbor in components:
                        components.remove(neighbor)
            visited.append(current)
            # print(current, stack, visited, components, connected)
        return connected


if __name__ == '__main__':
    print('in main')
    properties = [[2],[4],[5],[4],[4],[3]]
    k = 1
    print(Solution().numberOfComponents(properties, k))
