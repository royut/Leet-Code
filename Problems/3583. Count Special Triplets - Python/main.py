class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictNums = {}
        for i in range(len(nums)):
            if nums[i] in dictNums:
                dictNums[nums[i]].append(i)
            else:
                dictNums[nums[i]] = [i]
        # print(dictNums)
        countSpecialTriplets = 0
        for i in range(1, len(nums)-1):
            targetNum = nums[i] * 2
            # print(i, targetNum)
            if targetNum in dictNums and dictNums[targetNum][0] < i < dictNums[targetNum][-1]:
                # print(dictNums[targetNum])
                low, high = 0, len(dictNums[targetNum]) - 1
                while low < high:
                    mid = low + ((high - low + 1) >> 1)
                    # print(low, mid, high)
                    if dictNums[targetNum][mid] <= i:
                        low = mid
                    else:
                        high = mid - 1
                # print('res', low, mid, high)
                # print('multi', mid, len(dictNums[targetNum])-mid)
                # print(dictNums[targetNum][mid])
                if targetNum == nums[i]:
                    countSpecialTriplets += low * (len(dictNums[targetNum]) - 1 - low)
                else:
                    countSpecialTriplets += (low + 1) * (len(dictNums[targetNum]) - 1 - low)
        return countSpecialTriplets % 1000000007


if __name__ == "__main__":
    print('in main')
    nums = [6, 6, 3, 6]
    nums = [84, 2, 93, 1, 2, 2, 26]
    nums = [0, 1, 0, 0]
    print(Solution().specialTriplets(nums))