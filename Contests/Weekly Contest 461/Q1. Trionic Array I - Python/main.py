class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = 0
        way = 1
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > temp:
                if way == 1:
                    temp = nums[i]
                elif way == -1:
                    temp = nums[i]
                    way = 1
                    flag += 1
            elif nums[i] < temp:
                if way == -1:
                    temp = nums[i]
                elif way == 1:
                    temp = nums[i]
                    way = -1
                    flag += 1
            else:
                return False
        return flag == 2 and nums[0] < nums[1]


if __name__ == '__main__':
    print('in main')
    nums = [1, 3, 5, 4, 2, 6]
    nums = [2, 1, 3]
    nums = [4, 1, 5, 2, 3]
    print(Solution().isTrionic(nums))