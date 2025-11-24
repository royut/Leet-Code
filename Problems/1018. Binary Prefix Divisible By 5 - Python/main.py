class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        currNum = nums[0]
        results = [currNum % 5 == 0]
        # print(currNum, results)
        for i in range(1, len(nums)):
            currNum = currNum * 2 + nums[i]
            results.append(currNum % 5 == 0)
        return results


if __name__ == '__main__':
    print('in main')
    nums = [0, 1, 1]
    print(Solution().prefixesDivBy5(nums))