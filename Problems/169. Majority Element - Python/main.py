class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        maxNum = nums[0]
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
            if d[num] > d[maxNum]:
                maxNum = num
        return maxNum


if __name__ == '__main__':
    print(Solution().majorityElement([2,2,1,1,1,2,2]))