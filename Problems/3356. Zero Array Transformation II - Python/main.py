class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        left, right = 0, len(queries)

        if not self.canFormZeroArray(nums, queries, right):
            return -1

        while left <= right:
            mid = left + (right - left) // 2
            if self.canFormZeroArray(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


    def canFormZeroArray(self, nums, queries, k):
        n = len(nums)
        diffSum = 0
        diffArray = [0] * (n+1)
        for queryIndex in range(k):
            l, r, val = queries[queryIndex]
            diffArray[l] += val
            diffArray[r+1] -= val

        for i in range(n):
            diffSum += diffArray[i]
            if diffSum < nums[i]:
                return False
        return True


if __name__ == '__main__':
    print('in main')
    nums = [2, 0, 2]
    queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
    # nums = [4, 3, 2, 1]
    # queries = [[1, 3, 2], [0, 2, 1]]
    print(Solution().minZeroArray(nums, queries))
