class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # find index of 0
        i_0 = 0
        for i in range(n):
            if nums[i] == 0:
                i_0 = i
        # check if increasing
        inc_flag = True
        i = i_0 + 1
        while i-i_0 < n:
            # print(i, nums[(i-1) % n], nums[i % n])
            if nums[(i-1) % n] + 1 != nums[i % n]:
                inc_flag = False
                break
            i += 1
        # check if decreasing
        dec_flag = True
        i = i_0 - 1
        while abs(i-i_0) < n:
            # print(i, nums[i % n], nums[(i+1) % n])
            if nums[i % n] != nums[(i+1) % n] + 1:
                dec_flag = False
                break
            i -= 1

        if not inc_flag and not dec_flag:
            return -1
        if inc_flag:
            return min(i_0, n-i_0+2)
        else:
            return min(i_0+1, n-i_0-1) + 1


if __name__ == "__main__":
    print('in main')
    # nums = [2, 0, 1]
    # nums = [0, 3, 2, 1]
    nums = [1, 0, 2]
    # nums = [2, 0, 1, 3]
    # nums = [0, 2, 1]
    print(Solution().minOperations(nums))