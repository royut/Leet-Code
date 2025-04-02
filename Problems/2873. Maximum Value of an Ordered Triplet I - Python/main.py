class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = 0
        for i in range(len(nums)):
            for ii in range(i+1, len(nums)):
                for iii in range(ii+1, len(nums)):
                    # print(i,ii,iii)
                    if (nums[i] - nums[ii]) * nums[iii] > maxSoFar:
                        maxSoFar = (nums[i] - nums[ii]) * nums[iii]
        return maxSoFar


if __name__ == '__main__':
    print('in main')
    nums = [1, 10, 3, 4, 19]
    print(Solution().maximumTripletValue(nums))
