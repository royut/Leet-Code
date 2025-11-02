class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = nums[-1]
        i, j = nums[0], 1
        missing = []
        while i <= n:
            if i != nums[j-1]:
                missing.append(i)
            else:
                j += 1
            i += 1
        return missing


if __name__ == '__main__':
    print('in main')
    nums = [7, 8, 6, 9]
    nums = [5, 1]
    print(Solution().findMissingElements(nums))