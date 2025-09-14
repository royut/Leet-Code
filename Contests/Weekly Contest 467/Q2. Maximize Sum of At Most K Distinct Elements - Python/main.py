class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums = sorted(set(nums))[::-1]
        return nums[:k]


if __name__ == "__main__":
    print('in main')
    nums = [84,93,100,77,90,100]
    k = 3
    print(Solution().maxKDistinct(nums, k))