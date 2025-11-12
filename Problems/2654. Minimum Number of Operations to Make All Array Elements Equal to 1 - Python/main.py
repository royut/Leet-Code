class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        numsGcd = nums[0]
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            numsGcd = self.gcd(nums[i], numsGcd)

        if numsGcd != 1:
            return -1
        elif ones != 0:
            return len(nums) - ones

        minGcdLen = len(nums)
        for i in range(len(nums)):
            tempGcd = nums[i]
            for j in range(i + 1, len(nums)):
                tempGcd = self.gcd(tempGcd, nums[j])
                if tempGcd == 1:
                    minGcdLen = min(minGcdLen, j - i + 1)
                    break
        return minGcdLen - 1 + len(nums) - 1


if __name__ == "__main__":
    print('in main')
    nums = [2, 6, 3, 4]
    # nums = [2, 10, 6, 14]
    print(Solution().minOperations(nums))