class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top1, top2 = float("-inf"), float("-inf")
        for i in range(len(nums)):
            # print(top1, top2)
            if abs(nums[i]) > top1:
                top2 = top1
                top1 = abs(nums[i])
            elif abs(nums[i]) > top2:
                top2 = abs(nums[i])
        return top1 * top2 * (10 ** 5)


if __name__ == '__main__':
    print('in main')
    nums = [-5, 7, 0]
    print(Solution().maxProduct(nums))