class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        bunches = []
        tempSet = {0}
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= maxDiff:
                tempSet.add(i)
            else:
                bunches.append(tempSet)
                tempSet = {i}
        bunches.append(tempSet)
        # print(bunches)
        ans = []
        for s, e in queries:
            for bunch in bunches:
                if s in bunch and e in bunch:
                    ans.append(True)
                    break
                if s in bunch and e not in bunch:
                    ans.append(False)
                    break
        return ans


if __name__ == "__main__":
    print('in main')
    n = 2
    nums = [1, 3]
    maxDiff = 1
    queries = [[0, 0], [0, 1]]
    # n = 4
    # nums = [2, 5, 6, 8]
    # maxDiff = 2
    # queries = [[0, 1], [0, 2], [1, 3], [2, 3]]
    print(Solution().pathExistenceQueries(n, nums, maxDiff, queries))