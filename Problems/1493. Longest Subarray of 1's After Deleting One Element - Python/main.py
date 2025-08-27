class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        shortened = []
        if nums[0] == 0:
            shortened.append(-1)
        else:
            shortened.append(1)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                if shortened[-1] < 0:
                    shortened[-1] = shortened[-1] - 1
                else:
                    shortened.append(-1)
            else:
                if shortened[-1] > 0:
                    shortened[-1] = shortened[-1] + 1
                else:
                    shortened.append(1)
        # print(shortened)
        maxLen = 0
        for i in range(len(shortened)):
            if shortened[i] == -1:
                tempMax = 0
                if i > 0:
                    tempMax += shortened[i-1]
                if i < len(shortened) - 1:
                    tempMax += shortened[i+1]
                shortened[i] = tempMax
                if tempMax > maxLen:
                    maxLen = tempMax
            elif shortened[i] > 0:
                if shortened[i] > maxLen:
                    maxLen = shortened[i]
        if len(shortened) == 1 and shortened[0] > 0:
            return len(nums) - 1
        else:
            return maxLen


if __name__ == "__main__":
    print('in main')
    nums = [1, 1, 0, 1]
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    nums = [1, 1, 1]
    nums = [0, 0, 0]
    # nums = [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
    print(Solution().longestSubarray(nums))