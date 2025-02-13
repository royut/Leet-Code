class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return 0
        products = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # if i != j:
                if nums[i] * nums[j] not in products:
                    products[nums[i] * nums[j]] = 1
                else:
                    products[nums[i] * nums[j]] += 1
        # print(products)
        sumSameProduct = 0
        for product in products:
            if products[product] > 1:
                sumSameProduct += products[product] * (products[product] - 1) * 4
        return sumSameProduct


if __name__ == '__main__':
    print('in main')
    nums = [2, 3, 4, 6]
    nums = [1, 2, 4, 5, 10]
    nums = [2, 3, 4, 6, 8, 12]
    nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    print(Solution().tupleSameProduct(nums))
