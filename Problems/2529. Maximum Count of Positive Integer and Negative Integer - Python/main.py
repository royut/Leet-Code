class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        neg = 0
        negFlag = False
        pos = 0
        posFlag = False
        for i in range(len(nums)):
            if nums[i] >= 0 and not negFlag:
                neg = i
                negFlag = True
            if nums[i] > 0:
                pos = n-i
                break
            if nums[n-i-1] <= 0 and not posFlag:
                pos = i
                posFlag = True
            if nums[n-i-1] < 0:
                neg = n-i
                break
        return max(pos, neg)


if __name__ == '__main__':
    print('in main')
    nums = [-2,-1,-1,1,2,3]
    print(Solution().maximumCount(nums))