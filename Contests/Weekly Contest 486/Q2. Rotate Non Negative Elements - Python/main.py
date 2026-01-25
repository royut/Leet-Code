class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nonNegs = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                nonNegs.append(nums[i])
        n = len(nonNegs)
        if n == 0:
            return nums
        k = k % n
        # print(k)
        nonNegsRot = [-1 for _ in range(n)]
        for i in range(len(nonNegs)):
            # print(i, nonNegs[i])
            newI = i - k
            if newI < 0:
                newI += n
            nonNegsRot[newI] = nonNegs[i]
            # print(nonNegsRot)
        numsRot = [0 for _ in range(len(nums))]
        nonNegsIndex = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                numsRot[i] = nums[i]
            else:
                numsRot[i] = nonNegsRot[nonNegsIndex]
                nonNegsIndex += 1
        return numsRot


if __name__ == '__main__':
    print('in main')
    nums = [1, -2, 3, -4]
    k = 3
    nums = [5, 4, -9, 6]
    k = 2
    nums = [-3, -2, 7]
    k = 1
    print(Solution().rotateElements(nums, k))