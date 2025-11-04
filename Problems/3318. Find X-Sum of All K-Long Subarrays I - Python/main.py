class Solution(object):
    def XSum(self, nums, x):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freq = list(freq.items())
        freq.sort(key=lambda x: (x[1], x[0]), reverse=True)
        n = len(freq)
        XSum = 0
        for i in range(x):
            if i <= n - 1:
                XSum += freq[i][0] * freq[i][1]
        return XSum

    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            ans.append(self.XSum(nums[i:i+k], x))
            # print(self.XSum(nums[i:i+k], x))
        return ans


if __name__ == "__main__":
    print("in main")
    nums = [1, 1, 2, 2, 3, 4, 2, 3]
    k = 6
    x = 2
    print(Solution().findXSum(nums, k, x))