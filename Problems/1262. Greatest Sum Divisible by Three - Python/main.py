class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        numsSum = 0
        numsSumMod3 = 0
        mods = {0: [], 1: [], 2: []}
        for num in nums:
            numsSum += num
            mods[num % 3].append(num)
            if num % 3 == 0:
                numsSumMod3 += num
        # print(mods)
        if numsSum % 3 == 0:
            return numsSum
        elif numsSum % 3 == 1:
            if len(mods[2]) >= 2 and len(mods[1]) >= 1:
                minDec = min(mods[1][0], mods[2][0] + mods[2][1])
            elif len(mods[1]) >= 1:
                minDec = mods[1][0]
            else:
                return numsSumMod3
            return numsSum - minDec
        elif numsSum % 3 == 2:
            if len(mods[1]) >= 2 and len(mods[2]) >= 1:
                minDec = min(mods[2][0], mods[1][0] + mods[1][1])
            elif len(mods[2]) >= 1:
                minDec = mods[2][0]
            else:
                return numsSumMod3
            return numsSum - minDec
        return numsSumMod3


if __name__ == "__main__":
    print('in main')
    nums = [3, 6, 5, 1, 8]
    nums = [1, 1, 3]
    print(Solution().maxSumDivThree(nums))