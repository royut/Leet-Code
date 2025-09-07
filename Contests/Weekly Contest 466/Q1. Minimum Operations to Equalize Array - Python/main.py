class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) == 1:
            return 0
        else:
            return 1


if __name__ == "__main__":
    print('in main')
    nums = [1, 2]
    print(Solution().minOperations(nums))