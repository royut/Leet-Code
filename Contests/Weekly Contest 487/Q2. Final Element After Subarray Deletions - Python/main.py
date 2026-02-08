class Solution(object):
    def finalElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        alice = True
        bob = False
        while len(nums) > 1:
            minL, minT, minR = float('inf'), float('inf'), float('inf')
            maxL, maxT, maxR = -1, -1, -1
            for i in range(len(nums)):
                pass


if __name__ == "__main__":
    print('in main')
    nums = [1, 5, 2]
    print(Solution().finalElement(nums))