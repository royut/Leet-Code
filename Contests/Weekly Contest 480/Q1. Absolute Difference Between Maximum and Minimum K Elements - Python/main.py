class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        largest = 0
        smallest = 0
        print(nums)
        for i in range(k):
            smallest += nums[i]
            largest += nums[len(nums) - 1 - i]
        return abs(smallest - largest)


if __name__ == '__main__':
    print(Solution().absDifference([1,2,3,4,5], 3))