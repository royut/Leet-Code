class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lesser = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot:
                lesser.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return lesser + equal + greater


if __name__ == "__main__":
    print('in main')
    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    print(Solution().pivotArray(nums, pivot))