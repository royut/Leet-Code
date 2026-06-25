class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        prefix = [0] * (n+1)
        tempCount = 0
        for i in range(n):
            if nums[i] == target:
                tempCount += 1
            prefix[i+1] = tempCount

        # print('n', nums)
        # print('p', prefix)

        countMajorities = 0
        for i in range(n):
            for j in range(i, n):
                countTarget = prefix[j+1] - prefix[i]
                length = j - i + 1
                # print(i, j, length, nums[i:j+1], prefix[i], prefix[j+1], countTarget)
                if countTarget > length // 2:
                    countMajorities += 1
        return countMajorities


if __name__ == "__main__":
    print('in main')
    # nums = [1, 2, 2, 3]
    # target = 1
    nums = [1, 1, 1, 1]
    target = 1
    print(Solution().countMajoritySubarrays(nums, target))