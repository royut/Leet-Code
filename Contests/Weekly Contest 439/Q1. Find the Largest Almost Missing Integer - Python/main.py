class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numCounts = {}
        for i in range(len(nums)-k+1):
            subArray = set(nums[i:i+k])
            for num in subArray:
                if num not in numCounts:
                    numCounts[num] = 1
                else:
                    numCounts[num] += 1
        # print(numCounts)
        maxAlmostMissing = -1
        for num in numCounts:
            if numCounts[num] == 1 and num > maxAlmostMissing:
                # print(num, numCounts[num])
                maxAlmostMissing = num
        return maxAlmostMissing


if __name__ == '__main__':
    print('in main')
    nums = [3, 9, 2, 1, 7]
    k = 3
    nums = [3, 9, 7, 2, 1, 7]
    k = 4
    nums = [0, 0]
    k = 1
    print(Solution().largestInteger(nums, k))
