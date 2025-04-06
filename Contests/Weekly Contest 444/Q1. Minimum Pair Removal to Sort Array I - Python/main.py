class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        while True:
            pairSums = []
            minPairSum = float('inf')
            minPairSumIndex = 0
            nonDecreasing = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nonDecreasing = False
                pairSums.append(nums[i]+nums[i+1])
                if nums[i]+nums[i+1] < minPairSum:
                    minPairSum = nums[i]+nums[i+1]
                    minPairSumIndex = i
            if nonDecreasing:
                return operations
            nums[minPairSumIndex] = minPairSum
            nums.pop(minPairSumIndex+1)
            operations += 1


if __name__ == '__main__':
    print('in main')
    nums = [1,2,2]
    print(Solution().minimumPairRemoval(nums))