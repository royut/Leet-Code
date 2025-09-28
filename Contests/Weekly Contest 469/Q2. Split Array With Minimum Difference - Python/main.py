class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumFromStart = 0
        sumsFromStart = []
        sumFromEnd = 0
        sumsFromEnd = []
        length = len(nums)
        for i in range(len(nums)):
            sumFromStart += nums[i]
            sumsFromStart.append(sumFromStart)
            sumFromEnd += nums[len(nums) - i - 1]
            sumsFromEnd.append(sumFromEnd)
        # print(sumsFromStart)
        # print(sumsFromEnd)

        increasing = True
        shuffleCount = 0
        shuffleIndex = 1
        for i in range(1, len(nums)):
            if increasing and nums[i] > nums[i - 1]:
                pass
            elif not increasing and nums[i] < nums[i - 1]:
                pass
            else:
                increasing = not increasing
                shuffleCount += 1
                shuffleIndex = i
                if shuffleCount == 2:
                    return -1
        # print(shuffleCount)
        if shuffleCount == 0:
            shuffleIndex = length - 1
        # print(shuffleIndex)
        # print(nums[:shuffleIndex], nums[shuffleIndex:])
        diff = abs(sumsFromStart[shuffleIndex-1] - sumsFromEnd[length - shuffleIndex - 1])
        if nums[shuffleIndex-1] > nums[shuffleIndex] and shuffleIndex - 1 != 0:
            # print(nums[:shuffleIndex-1], nums[shuffleIndex-1:])
            newDiff = abs(sumsFromStart[shuffleIndex-2] - sumsFromEnd[length - shuffleIndex])
            diff = min(diff, newDiff)
        return diff


if __name__ == "__main__":
    nums = [1, 2, 4, 3]
    # nums = [1, 3, 2]
    # nums = [1, 2, 1]
    # nums = [4,3]
    # nums = [2,4]
    nums = [77, 34, 23, 15, 5]
    nums = [1, 2, 3]
    print(Solution().splitArray(nums))