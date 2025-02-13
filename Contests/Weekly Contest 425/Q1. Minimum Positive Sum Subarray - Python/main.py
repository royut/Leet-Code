class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        min = 0
        for i in range(l, r+1):
            for j in range(i, len(nums) + 1):
                count = 0
                for k in range(j - i, j):
                    count += nums[k]
                if min == 0 and count > 0:
                    min = count
                elif count < min and count > 0:
                    min = count

        if min > 0:
            return min
        else:
            return -1


if __name__ == '__main__':
    print("in main")
    print(Solution().minimumSumSubarray([7, 3], 2, 2))