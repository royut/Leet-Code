class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        preProducts = [None]
        postProducts = [None]
        preProduct = nums[-1]
        postProduct = nums[0]
        for i in range(1, len(nums)):
            postProducts.append(postProduct)
            postProduct *= nums[i]
            preProducts.append(preProduct)
            preProduct *= nums[len(nums) - i - 1]
        # print(postProducts)
        preProducts.reverse()
        # print(preProducts)
        products = []
        for i in range(len(nums)):
            if preProducts[i] is None:
                products.append(postProducts[i])
            elif postProducts[i] is None:
                products.append(preProducts[i])
            else:
                products.append(preProducts[i] * postProducts[i])

        return products


if __name__ == '__main__':
    print("in main")
    nums = [-1,1,0,-3,3]
    print(nums)
    print(Solution().productExceptSelf(nums))
