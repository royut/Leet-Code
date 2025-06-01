class Solution(object):
    def checkEqualPartitions(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        product = 1
        for i in nums:
            product *= i
        if product == target * target:
            return True
        return False


if __name__ == '__main__':
    print('in main')
