class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniques = set(nums)
        print(uniques)
        n = len(nums)
        countCompletes = 0
        for i in range(n):
            temp = set()
            for j in range(i, n):
                # print(nums[i:j], nums[j])
                if nums[j] not in temp:
                    temp.add(nums[j])
                if temp == uniques:
                    countCompletes += 1
        return countCompletes


if __name__ == '__main__':
    print('in main')
    nums = [1, 3, 1, 2, 2]
    nums = [5, 5, 5, 5]
    print(Solution().countCompleteSubarrays(nums))