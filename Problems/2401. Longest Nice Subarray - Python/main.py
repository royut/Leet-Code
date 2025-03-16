class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, min(len(nums), 30)
        result = 1
        while left <= right:
            length = left + (right - left) // 2
            # print(left, right, length)
            if self.niceSubarrayPossible(nums, length):
                result = length
                left = length + 1
            else:
                right = length - 1
        return result

    def niceSubarrayPossible(self, nums, length):
        if length <= 1:
            return True
        for start in range(len(nums)-length+1):
            andBit = 0
            niceFlag = True
            for pos in range(start, start+length):
                if nums[pos] & andBit != 0:
                    niceFlag = False
                    break
                andBit |= nums[pos]
            if niceFlag:
                return True
        return False


if __name__ == '__main__':
    print('in main')
    nums = [1, 3, 8, 48, 10]
    print(Solution().longestNiceSubarray(nums))
    # print(2 & 1)
