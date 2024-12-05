class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first = 0
        last = len(nums) - 1
        final = []
        while first <= last:
            if abs(nums[first]) > abs(nums[last]):
                final.insert(0, pow(nums[first], 2))
                first += 1
            else:
                final.insert(0, pow(nums[last], 2))
                last -= 1
        return final


if __name__ == "__main__":
    print("in main")
    print(Solution().sortedSquares([-7,-3,2,3,11]))