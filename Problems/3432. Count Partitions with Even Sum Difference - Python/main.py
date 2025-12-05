class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i-1])
        # print(prefix)
        total = 0
        for i in range(1, len(nums)):
            if abs(prefix[i-1] - (prefix[-1] - prefix[i-1])) % 2 == 0:
                total += 1
        return total


if __name__ == "__main__":
    print('in main')
    nums = [10, 10, 3, 7, 6]
    print(Solution().countPartitions(nums))