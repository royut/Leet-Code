class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        nums.sort()
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        # print(freq)
        maxFreq = 0
        for i in range(nums[0], nums[-1] + 1):
            tempFreq = 0
            tempOperations = numOperations
            for j in range(-k, k + 1):
                if i + j in freq:
                    if j == 0:
                        tempFreq += freq[i + j]
                    elif tempOperations > 0:
                        tempFreq += min(tempOperations, freq[i + j])
                        tempOperations -= min(tempOperations, freq[i + j])
                # print(j, tempFreq, i, tempOperations)
            # print(i, tempFreq)
            if tempFreq > maxFreq:
                maxFreq = tempFreq
        return maxFreq


if __name__ == '__main__':
    print('in main')
    # nums = [1, 4, 5]
    # k = 1
    # numOperations = 2
    nums = [5, 11, 20, 20]
    k = 5
    numOperations = 1
    print(Solution().maxFrequency(nums, k, numOperations))