class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        endpoints = [-1] * n
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= maxDiff:
                pass
            else:
                endpoints[i-1] = i-1
        endpoints[n-1] = n-1
        tempEndpoint = n-1
        for i in range(len(nums)-2, -1, -1):
            if endpoints[i] == -1:
                endpoints[i] = tempEndpoint
            else:
                tempEndpoint = endpoints[i]
        print(endpoints)
        ans = []
        for s, e in queries:
            s, e = min(s, e), max(s, e)
            # print(endpoints[s])
            if e <= endpoints[s]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


if __name__ == "__main__":
    print('in main')
    # n = 2
    # nums = [1, 3]
    # maxDiff = 1
    # queries = [[0, 0], [0, 1]]
    # n = 4
    # nums = [2, 5, 6, 8]
    # maxDiff = 2
    # queries = [[0, 1], [0, 2], [1, 3], [2, 3]]
    n, nums, maxDiff, queries = 2, [2975, 50642], 6, [[1, 0]]
    print(Solution().pathExistenceQueries(n, nums, maxDiff, queries))