class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxes = [nums[0]]
        maxInMaxes = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maxInMaxes:
                maxInMaxes = nums[i]
            maxes.append(maxInMaxes)
        # print(maxes)
        maxesFromEnd = [nums[-1]]
        maxInMaxes = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > maxInMaxes:
                maxInMaxes = nums[i]
            maxesFromEnd.append(maxInMaxes)
        # print(maxesFromEnd)
        maxSoFar = 0
        for j in range(1, len(nums)-1):
            max1 = maxes[j-1]
            max2 = maxesFromEnd[len(nums)-2-j]
            temp = (max1 - nums[j]) * max2
            maxSoFar = max(maxSoFar, temp)
            # print(j, max1, max2, temp)
        return maxSoFar


if __name__ == '__main__':
    print('in main')
    nums = [1, 10, 3, 4, 19]
    nums = [10, 13, 6, 2]
    print(Solution().maximumTripletValue(nums))