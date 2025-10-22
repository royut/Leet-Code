import bisect

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
        print(nums)
        maxFreq = 0
        for i in range(nums[0], nums[-1] + 1):
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1
            len = r - l + 1
            if i in freq:
                tempFreq = min(len, freq[i] + numOperations)
            else:
                tempFreq = min(len, numOperations)
            maxFreq = max(maxFreq, tempFreq)
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