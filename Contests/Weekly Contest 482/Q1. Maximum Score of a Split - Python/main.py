class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        suffix_min = [0] * len(nums)
        temp_min = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < temp_min:
                temp_min = nums[i]
            suffix_min[i] = temp_min
        max_score = prefix_sum[0] - suffix_min[1]
        for i in range(len(nums)-1):
            # print(prefix_sum[i], suffix_min[i+1], prefix_sum[i] - suffix_min[i+1])
            if prefix_sum[i] - suffix_min[i+1] > max_score:
                max_score = prefix_sum[i] - suffix_min[i+1]
        return max_score


if __name__ == '__main__':
    print('in main')
    nums = [10, -1, 3, -4, -5]
    nums = [-7, -5, 3]
    print(Solution().maximumScore(nums))