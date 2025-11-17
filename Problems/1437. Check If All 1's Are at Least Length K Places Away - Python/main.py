class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        countingZeroes = 0
        countingFlag = False
        startFlag = False
        for num in nums:
            if num == 1 and not startFlag:
                startFlag = True
            elif startFlag:
                if num == 1:
                    print(countingZeroes)
                    if countingZeroes < k:
                        return False
                    countingFlag = False
                    countingZeroes = 0
                elif num == 0 and not countingFlag:
                    countingZeroes = 1
                    countingFlag = True
                elif num == 0 and countingFlag:
                    countingZeroes += 1
            # print(countingZeroes)
        return True


if __name__ == '__main__':
    print('in main')
    nums = [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    k = 2
    # nums = [1, 0, 0, 1, 0, 1]
    # k = 2
    print(Solution().kLengthApart(nums, k))