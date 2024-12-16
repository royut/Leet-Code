class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(nums) - sum(set(nums))) / (len(nums) - len(set(nums)))


if __name__ == '__main__':
    print("in main")
    print(Solution().findDuplicate([1,3,4,2,2]))
