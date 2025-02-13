class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.nums[left:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))
