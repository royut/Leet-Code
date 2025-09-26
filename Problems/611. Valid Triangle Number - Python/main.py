class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countTriangles = 0
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            k = i + 2
            for j in range(i+1, n-1):
                if nums[i] == 0:
                    break
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                countTriangles += k - j - 1
        return countTriangles


if __name__ == "__main__":
    print('in main')
    nums = [2, 2, 3, 4]
    # nums = [4, 2, 3, 4]
    print(Solution().triangleNumber(nums))