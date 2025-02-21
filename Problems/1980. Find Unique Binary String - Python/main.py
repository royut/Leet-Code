class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        nums = list(set(nums))
        # print(nums)
        n = len(nums[0])
        validNums = list(range(pow(2, n)))
        for num in nums:
            numInTen = 0
            for i in range(n):
                numInTen += int(num[-i-1]) * pow(2, i)
            validNums.remove(numInTen)
        validNum = validNums.pop()
        print(validNum)
        validNumStr = ""
        for i in range(n):
            validNumStr = str(validNum % 2) + validNumStr
            validNum = validNum // 2
        return validNumStr


if __name__ == '__main__':
    print('in main')
    nums = ["111", "011", "001", "001"]
    # nums = ["1"]
    # nums = ["10", "11"]
    # nums = ["01", "10"]
    print(Solution().findDifferentBinaryString(nums))
