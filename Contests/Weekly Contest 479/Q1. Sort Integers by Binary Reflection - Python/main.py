class Solution(object):
    def compare(self, num1, num2):
        rNum1 = int(bin(num1)[2:][::-1].lstrip('0'), 2)
        rNum2 = int(bin(num2)[2:][::-1].lstrip('0'), 2)
        if rNum1 > rNum2:
            return 1
        elif rNum1 < rNum2:
            return -1
        else:
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                return 0

    def sortByReflection(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if self.compare(nums[i], nums[j]) == 1:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    print('in main')
    nums = [4, 5, 4]
    nums = [3, 6, 5, 8]
    print(Solution().sortByReflection(nums))