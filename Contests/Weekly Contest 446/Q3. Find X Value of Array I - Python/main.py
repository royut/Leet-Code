class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        productsFromStart = [1]
        products = 1
        for i in range(n):
            products *= nums[i]
            productsFromStart.append(products)
        # print(productsFromStart)
        # print(nums)
        remainders = k * [0]
        for i in range(n):
            for j in range(i, n):
                remainders[(productsFromStart[j + 1] // productsFromStart[i]) % k] += 1
        # print(remainders)
        return remainders


if __name__ == '__main__':
    print('in main')
    nums = [1, 2, 3, 4, 5]
    k = 3
    nums = [1, 2, 4, 8, 16, 32]
    k = 4
    nums = [1, 1, 2, 1, 1]
    k = 2
    print(Solution().resultArray(nums, k))