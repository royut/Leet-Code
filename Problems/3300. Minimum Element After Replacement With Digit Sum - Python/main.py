class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minSum = float('inf')
        for i in range(len(nums)):
            num = nums[i]
            temp = 0
            while num > 0:
                temp += num % 10
                num = num // 10
            if temp < minSum:
                minSum = temp
        return minSum


if __name__ == "__main__":
    print('in main')
    arr = [10, 12, 13, 14]
    print(Solution().minElement(arr))