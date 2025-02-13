class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums)
        dups = set()
        for i in nums:
            try:
                n.remove(i)
            except:
                pass
                dups.add(i)
        for i in (set(nums) - dups):
            return i


if __name__ == '__main__':
    print(Solution().singleNumber([1]))
