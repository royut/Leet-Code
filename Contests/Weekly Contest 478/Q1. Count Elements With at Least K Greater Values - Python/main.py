class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        n = len(nums)
        if k == 0:
            return n
        countReps = 0
        countQualified = 0
        # print(nums, n)
        while i < n-1:
            if nums[i] == nums[i+1]:
                countReps += 1
            else:
                if n - i - 1 >= k:
                    # print(nums[i], 'pass')
                    countQualified += 1 + countReps
                countReps = 0
            i += 1
        return countQualified


if __name__ == '__main__':
    print('in main')
    nums = [3, 1, 2]
    k = 1
    nums = [332931278, 226558367, 744830869]
    k = 2
    print(Solution().countElements(nums, k))