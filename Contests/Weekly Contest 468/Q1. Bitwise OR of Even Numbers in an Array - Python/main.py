class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        products = 0
        for num in nums:
            if num % 2 == 0:
                products |= num
        return products


if __name__ == "__main__":
    print('in main')
    nums = [1,2,3,4,5,6]
    print(Solution().evenNumberBitwiseORs(nums))