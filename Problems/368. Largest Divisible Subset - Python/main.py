class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        cache = {}

        def dfs(i, prev):
            # print(i, prev)
            if i == len(nums):
                return []
            if (i, prev) in cache:
                return cache[(i, prev)]

            res = dfs(i+1, prev)
            if nums[i] % prev == 0:
                temp = [nums[i]] + dfs(i+1, nums[i])
                if len(temp) > len(res):
                    res = temp

            cache[(i, prev)] = res
            # print(res, cache)
            return res

        return dfs(0, 1)


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3]
    nums = [1, 2, 4, 8]
    nums = [2, 3, 4, 8, 9]
    # nums = [5,9,18,54,108,540,90,180,360,720]
    print(Solution().largestDivisibleSubset(nums))