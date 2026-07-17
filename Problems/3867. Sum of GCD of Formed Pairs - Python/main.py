class Solution(object):
    def calcGCD(self, a, b):
        a, b = max(a, b), min(a, b)
        while True:
            if a % b == 0:
                return b
            a, b = b, a % b

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd = []
        tempMax = nums[0]
        for num in nums:
            if num > tempMax:
                tempMax = num
            prefixGcd.append(self.calcGCD(num, tempMax))
        prefixGcd = sorted(prefixGcd)
        # print(prefixGcd)
        index = 0
        sumGcd = 0
        while index < len(prefixGcd) // 2:
            # print(index, prefixGcd[index], prefixGcd[-(index + 1)])
            sumGcd += self.calcGCD(prefixGcd[index], prefixGcd[-(index + 1)])
            index += 1
        return sumGcd


if __name__ == "__main__":
    print('in main')
    nums = [2, 6, 4]
    nums = [3, 6, 2, 8]
    print(Solution().gcdSum(nums))
