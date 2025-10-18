class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        lowest, highest = nums[0] - k, nums[-1] + k
        n = len(nums)
        # print(lowest, highest, highest - lowest + 1)
        nums[0] -= k
        for i in range(1, n):
            goal = nums[i-1]+1
            # print(i, nums[i], goal)
            if goal - k <= nums[i] <= goal + k:
                nums[i] = goal
            else:
                # print('oof')
                if nums[i] < goal:
                    nums[i] += k
                else:
                    nums[i] -= k
        # print(nums)
        return len(set(nums))


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 2, 3, 3, 4]
    k = 2
    nums = [4, 4, 4, 4]
    k = 1
    # nums = [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5]
    # k = 3
    # nums = [56, 56, 54, 54]
    # k = 0
    print(Solution().maxDistinctElements(nums, k))
